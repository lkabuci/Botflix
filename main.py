from utils import utils
from utils.utils import start_scrawling, PrintColor
from src.stream import get_magnet


YES_CHOICES = ["", "y", "yes"]
NO_CHOICES = ["no", "n"]
EXIT_CHOICES = ['exit', 'quit']


is_choice_valid = True

while is_choice_valid:
    answer = input('Do you want to get top movies? (Y/N)  ').strip().lower()
    if answer in YES_CHOICES:
        from src.scrapping.scrapping.spiders.topmovies_spider import TopMoviesSpider
        movies = start_scrawling(TopMoviesSpider)
        utils.clear_screen()
        magnets = [movie['link'] for movie in movies]
        get_magnet(magnets)
        is_choice_valid = False
    
    elif answer in NO_CHOICES:
        from src.scrapping.scrapping.spiders.searched_movies import SearchedMoviesSpider
        movies = start_scrawling(SearchedMoviesSpider)
        utils.clear_screen()
        magnets = [movie['link'] for movie in movies]
        get_magnet(magnets)
        is_choice_valid = False
        
    else:
        utils.clear_screen()
        PrintColor.red(f'"{answer}" is not a valid choice, please enter a valid choice.')
        PrintColor.yellow(f"valid choices are ({', '.join(YES_CHOICES[1:])}) or ({', '.join(NO_CHOICES)})")
        PrintColor.yellow(f"type ({', '.join(EXIT_CHOICES)}) to quit the stream-cli.")
