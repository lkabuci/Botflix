from typing import Callable, Generator, List
from scrapy.crawler import CrawlerProcess
import sys, os
  
def clear_screen() -> None:
    # for windows 'nt' else for unix
    os.system('cls') if os.name == 'nt' else os.system('clear')


def start_scrawling(spider_class: Callable[[], Generator]) -> List[dict]:
    """takes a spider class as an argument ( TopMoviesSpider or SearchedMoviesSpider )
    return a list of movies inside a dictionnary
    """
    
    process = CrawlerProcess()
    process.crawl(spider_class)
    process.start()
        
    # exit if result is null
    if spider_class.output == []:
        clear_screen()
        sys.exit("\033[91mNo results returned. Refine your search term. It may also be a problem with your vpn.\033[0m")
        
    return spider_class.output
