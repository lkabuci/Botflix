from utils import utils
from utils.utils import start_scrawling
from src.stream import get_magnet, stream
from src.player import check_player
from src.interface import print_table_of_movies

import typer


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


if __name__ == "__main__":
    app()