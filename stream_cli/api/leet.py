from typing import Dict, List, Optional

import scrapy
from rich.console import Console

from helper.utils import handle_errors

MOVIES = "tbody tr"
MOVIE_INFO = "div.torrent-detail-page"
TITLE = "div h1::text"
SIZE = "div.no-top-radius div.clearfix ul.list li:nth-child(4) span::text"
SEEDS = "div.no-top-radius div.clearfix ul.list:nth-child(3) li:nth-child(4) span::text"
LEECHES = (
    "div.no-top-radius div.clearfix ul.list:nth-child(3) li:nth-child(5) span::text"
)
VIEWS = "div.no-top-radius div.clearfix ul.list:nth-child(3) li span::text"
DOMAIN = "https://1337x.to"
PAGE_INFO = "td a:nth-child(2)::attr(href)"
MAGNET = "div.no-top-radius div.clearfix ul li a::attr(href)"


handle_errors("https://www.1337x.to/")
console = Console()


def leet(category: Optional[str] = None):
    def _set_category() -> str:
        """return the target url"""

        if category is None:
            return "https://1337x.to/popular-movies"

        else:
            name = console.input("[bold]What are you looking for? ")
            converted_name = (
                "%20".join(name.split()) + "%207" if name is not None else None
            )

            if category == "movie":
                return (
                    f"https://1337x.to/category-search/{converted_name}%207/Movies/1/"
                )

            elif category == "serie":
                return f"https://1337x.to/category-search/{converted_name}%207/TV/1/"

    class _Leet(scrapy.Spider):

        output: List[Dict] = []
        idx: int = 1
        name: str = "leet"
        url: str = _set_category()

        start_urls = [url]
        limit = 20

        def parse(self, response):
            movies = response.css(MOVIES)
            for idx, movie in enumerate(movies, start=1):
                if idx <= _Leet.limit:
                    page_info = (
                        DOMAIN + movie.css("td a:nth-child(2)::attr(href)").get()
                    )
                    yield response.follow(page_info, callback=self.parse_movie)
                else:
                    break

        def parse_movie(self, response):

            for info in response.css(MOVIE_INFO):
                items = {
                    "index": _Leet.idx,
                    "title": info.css(TITLE).get().strip(),
                    "size": info.css(SIZE).get(),
                    "seeds": info.css(SEEDS).get(),
                    "leeches": info.css(LEECHES).get(),
                    "views": info.css(VIEWS).get(),
                    "magnet": info.css(MAGNET).get(),
                }
            _Leet.output.append(items)
            _Leet.idx += 1
            yield items

    return _Leet
