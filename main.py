from utils import utils
from utils.utils import start_scrawling, PrintColor
from src.stream import get_magnet, stream
from src.player import check_player
from src.interface import print_table_of_movies

YES_CHOICES = ["", "y", "yes"]
NO_CHOICES = ["no", "n"]
EXIT_CHOICES = ['exit', 'quit']

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
    

is_choice_valid = True

while is_choice_valid:
    answer = input('Do you want to get top movies? (Y/N)  ').strip().lower()
    if answer in YES_CHOICES:
        from src.scrapping.scrapping.spiders.topmovies_spider import TopMoviesSpider
        apprun(TopMoviesSpider, True)
        is_choice_valid = False
    
    elif answer in NO_CHOICES:
        from src.scrapping.scrapping.spiders.searched_movies import SearchedMoviesSpider
        apprun(SearchedMoviesSpider, is_top_movies_choice=False)
        is_choice_valid = False
        
    else:
        utils.clear_screen()
        PrintColor.red(f'"{answer}" is not a valid choice, please enter a valid choice.')
        PrintColor.yellow(f"valid choices are ({', '.join(YES_CHOICES[1:])}) or ({', '.join(NO_CHOICES)})")
        PrintColor.yellow(f"type ({', '.join(EXIT_CHOICES)}) to quit the stream-cli.")