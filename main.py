from utils.utils import PLAYERS_LIST
from utils import utils
from src.runner import apprun

import typer
from rich import print

from pathlib import Path


app = typer.Typer()


@app.command(short_help="get table of top movies")
def top():
    if utils.is_player_valid():
        from src.scrapping.scrapping.spiders.topmovies_spider import TopMoviesSpider

        apprun(TopMoviesSpider, True)
    else:
        print(
            "[red]Something went wrong, try python3 main.py config 'default_player'[red]"
        )
        exit(1)


@app.command(short_help="search for a specific movie")
def search():
    if utils.is_player_valid():
        from src.scrapping.scrapping.spiders.searched_movies import SearchedMoviesSpider

        apprun(SearchedMoviesSpider, is_top_movies_choice=False)
    else:
        print(
            "[red]Something went wrong, try python3 main.py config 'default_player'[red]"
        )
        exit(1)


@app.command(short_help="search for a specific TVSerie")
def serie():
    if utils.is_player_valid():
        from src.scrapping.scrapping.spiders.series import SeriesSpider

        apprun(SeriesSpider, is_top_movies_choice=False)
    else:
        print(
            "[red]Something went wrong, try python3 main.py config 'default_player'[red]"
        )
        exit(1)


@app.command(short_help="setup the default player")
def config(player: str):
    player = player.lower()
    if player not in PLAYERS_LIST:
        utils.wrong_player(player)
    else:
        directory = Path("config/")
        if not directory.exists():
            directory.mkdir()
        with open("config/player.txt", "w") as file:
            file.write(player)

        print(f'[bold green]Now "{player}" is your default media player!')


if __name__ == "__main__":
    app()
