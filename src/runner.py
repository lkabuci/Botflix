from src.stream import stream, get_magnet
from src.interface import print_table_of_movies
from utils.utils import CONFIG_PATH
from utils import utils

from scrapy.crawler import CrawlerProcess

from typing import Callable, Generator, List
from pathlib import Path
import sys


def start_scrawling(spider_class: Callable[[], Generator]) -> List[dict]:
    """takes a spider class as an argument ( TopMoviesSpider or SearchedMoviesSpider )
    return a list of movies inside a dictionnary
    """
    
    process = CrawlerProcess()
    process.crawl(spider_class)
    process.start()
        
    # exit if result is null
    if spider_class.output == []:
        utils.clear_screen()
        sys.exit("\033[91mUnable to connect to torrent provider. Please use vpn. Exiting...\033[0m")
        
    return spider_class.output

def apprun(chosenOptionClass, is_top_movies_choice: bool) -> None:
    movies = start_scrawling(chosenOptionClass)
     
    utils.clear_screen()
    if is_top_movies_choice:
        print_table_of_movies(movies, is_top_movies_choice=True)
    else:
        print_table_of_movies(movies, is_top_movies_choice=False)
    magnets = [movie['link'] for movie in movies]
    magnet = get_magnet(magnets)
    
    player = Path(CONFIG_PATH).read_text()
    stream(magnet, default_player=player)