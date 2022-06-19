from helper.utils import handle_erros

import scrapy
from scrapy.crawler import CrawlerProcess

from typing import Optional

MOVIES = "div.tgxtable div.tgxtablerow"
TITLE = "div.textshadow div a.txlight b::text"
SIZE = "div span.badge::text"
SEEDS = "div span font[color='green'] b::text"
LEECHES = "div span font[color='#ff0000'] b::text"
VIEWS = "div span[title='Views'] font b::text"
LINKS = "div[style='text-align:center;width:52px;padding-bottom:0px;padding-top:5px;'] a:nth-child(2)::attr(href)"

handle_erros("https://www.torrentgalaxy.to/")


def torrent_galaxy(category: str = None, name: Optional[str] = None):
    def _set_category() -> str:
        """return the target url"""

        converted_name = "+".join(name.split()) if name is not None else None

        if (category is None) or (name is None):
            return "https://torrentgalaxy.to/"

        elif category == "movie":
            return f"https://torrentgalaxy.to/torrents.php?c3=1&c46=1&c45=1&c42=1&c4=1&c1=1&search={converted_name}&sort=seeders&order=desc&lang=0&nox=2&nox=1#results"

        elif category == "serie":
            return f"https://torrentgalaxy.to/torrents.php?c41=1&c5=1&c6=1&search={converted_name}&lang=0&nox=1&sort=seeders&order=desc"

    # def _set_limit_results() -> int:
    #     """return the limit of results as int"""

    #     limit_results = ask_for_limit()
    #     return 50 if limit_results > 50 else limit_results

    class _TorrentGalaxy(scrapy.Spider):

        output = []
        name = "tgx"
        url = _set_category()

        start_urls = [url]
        limit = 20

        def parse(self, response):

            movies = response.css(MOVIES)
            for idx, movie in enumerate(movies, start=1):
                if idx <= _TorrentGalaxy.limit:
                    items = {
                        "index": idx,
                        "title": movie.css(TITLE).get(),
                        "size": movie.css(SIZE).get(),
                        "seeds": movie.css(SEEDS).get(),
                        "leeches": movie.css(LEECHES).get(),
                        "views": movie.css(VIEWS).get(),
                        "magnet": movie.css(LINKS).get(),
                    }
                    _TorrentGalaxy.output.append(items)
                    yield items
                else:
                    break

    return _TorrentGalaxy


# This is just for testing the spider manually
if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "LOG_LEVEL": "ERROR",
            "USER_AGENT": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        }
    )

    spider_class = torrent_galaxy(name="stranger things", category="serie")
    process.crawl(spider_class)
    process.start()
    # print(spider_class.output)
    print(len(spider_class.output))
