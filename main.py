from unittest.mock import DEFAULT
from utils import utils
from utils.utils import start_scrawling
from src.stream import get_magnet, stream
from src.player import check_player
from src.interface import print_table_of_movies

import typer
from rich import print

from pathlib import Path

DAFAULT_PLAYERS = ['vlc', 'mpv', 'mplayer']

app = typer.Typer()


def apprun(chosenOptionClass, is_top_movies_choice: bool) -> None:
    movies = start_scrawling(chosenOptionClass)
     
    utils.clear_screen()
    if is_top_movies_choice:
        print_table_of_movies(movies, is_top_movies_choice=True)
    else:
        print_table_of_movies(movies, is_top_movies_choice=False)
    magnets = [movie['link'] for movie in movies]
    magnet = get_magnet(magnets)
    player = check_player()
    stream(magnet, default_player=player)
    

@app.command(short_help='get table of top movies')
def top():
    from src.scrapping.scrapping.spiders.topmovies_spider import TopMoviesSpider
    apprun(TopMoviesSpider, True)


@app.command(short_help='search for a specific movie')
def search():
    from src.scrapping.scrapping.spiders.searched_movies import SearchedMoviesSpider
    apprun(SearchedMoviesSpider, is_top_movies_choice=False)


@app.command(short_help='setup the default player')
def config(player: str):
    player = player.lower()
    if player not in DAFAULT_PLAYERS:
        print(f"[bold red]Operation failed [u]{player}[/u] is not a valid player[bold red]")
        print(f"[bold yellow]Hint: the supported players are vlc, mpv and mplayer[/bold yellow]")
        print(f"[bold]Try again with one of the supported players[/bold]")
        exit(1)
    else:    
        directory = Path("config/")
        if not directory.exists():
            directory.mkdir()
        with open("config/player.txt", "w") as file:
            file.write(player)

        print(f'[bold green]Now "{player}" is your default media player!')
    
    

if __name__ == "__main__":
    app()