from typing import Callable, Generator, List
from scrapy.crawler import CrawlerProcess
from os import system, name
  
def clear_screen() -> None:
    # for windows 'nt' else for unix
    system('cls') if name == 'nt' else system('clear')


def start_scrawling(spider_class: Callable[[], Generator]) -> List[dict]:
    """takes a spider class as an argument ( TopMoviesSpider or SearchedMoviesSpider )
    return a list of movies inside a dictionnary
    """
    
    process = CrawlerProcess()
    process.crawl(spider_class)
    process.start()
    return spider_class.output


class PrintColor:
    
    def red(element_to_print: str) -> None: 
        print(f"\033[91m{element_to_print}\033[0m")
    
    def green(element_to_print: str) -> None:
        print(f"\033[92m{element_to_print}\033[0m")
        
    def yellow(element_to_print: str) -> None:
        print(f"\033[93m{element_to_print}\033[0m")