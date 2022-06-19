from pathlib import Path
from typing import Callable, Generator, List

import requests
from rich import print
from scrapy.crawler import CrawlerProcess

from helper import utils
from helper.user_angent import get_user_agent
from helper.utils import CONFIG_PATH
from stream_cli.interface import print_table_of_movies
from stream_cli.stream import get_magnet, stream


def start_scrawling(spider_class: Callable[[], Generator]) -> List[dict]:
    """takes a spider class as an argument ( TopMoviesSpider or SearchedMoviesSpider )
    return a list of movies inside a dictionnary
    """

    process = CrawlerProcess(
        settings={
            "LOG_LEVEL": "ERROR",
            "USER_AGENT": get_user_agent(),
        }
    )
    process.crawl(spider_class)
    process.start()

    # exit if result is null
    utils.clear_screen()
    if spider_class.output == []:
        response = requests.get("https://www.torrentgalaxy.to/").status_code
        if response != 200:
            print(
                "[bold red]Unable to connect to torrent provider. Please use vpn. Exiting[/bold red]"
            )
        else:
            print("[bold red]Movie Not Found Error[/bold red]")
        exit(1)

    return spider_class.output


def apprun(scraping_class) -> None:
    movies = start_scrawling(scraping_class)

    utils.clear_screen()
    print_table_of_movies(movies)
    magnets = [movie["magnet"] for movie in movies]
    magnet = get_magnet(magnets)

    player = Path(CONFIG_PATH).read_text()
    stream(magnet, default_player=player)
