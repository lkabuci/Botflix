import scrapy
from scrapy.crawler import CrawlerProcess

from typing import Optional

MOVIES = "div.tgxtable div.tgxtablerow"
TITLE = "div.textshadow div a.txlight b::text"
SIZE = "div span.badge::text"
SEEDS = "div span[title='Seeders/Leechers'] font b::text"
VIEWS = "div span[title='Views'] font b::text"
LINKS = "div[style='text-align:center;width:52px;padding-bottom:0px;padding-top:5px;'] a:nth-child(2)::attr(href)"

def torrent_galaxy(name: Optional[str], category: str, limit_results: int):

    def _set_category() -> str:
        """return the target url"""

        if category == "movie":
            return f"https://torrentgalaxy.to/torrents.php?c3=1&c46=1&c45=1&c42=1&c4=1&c1=1&search={name}&sort=seeders&order=desc&lang=0&nox=2&nox=1#results"
        elif category == "serie":
            return f"https://torrentgalaxy.to/torrents.php?c41=1&c5=1&c6=1&search={name}&lang=0&nox=1&sort=seeders&order=desc"
        elif category == "top":
            return "https://torrentgalaxy.to/"

    def _set_limit() -> int:
        """return the limit of results as int"""

        return 50 if limit_results > 50 else limit_results

    class _TorrentGalaxy(scrapy.Spider):

        output = []
        name = "tgx"
        url = _set_category()

        start_urls = [url]

        def parse(self, response):

            limit = _set_limit()

            movies = response.css(MOVIES)
            for idx, movie in enumerate(movies, start=1):
                if idx <= limit:
                    items = {
                        "index": idx,
                        "title": movie.css(TITLE).get(),
                        "size": movie.css(SIZE).get(),
                        "seeds": "/".join(movie.css(SEEDS).getall()[:2]),
                        "views": movie.css(VIEWS).get(),
                        "link": movie.css(LINKS).get(),
                    }
                    _TorrentGalaxy.output.append(items)
                    yield items

    return _TorrentGalaxy


# This is just for testing the spider manually
if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            # "LOG_LEVEL": "ERROR",
            "USER_AGENT": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        }
    )

    spider_class = torrent_galaxy(category="movie", name="red notice", limit_results=15)
    process.crawl(spider_class)
    process.start()
    # print(spider_class.output)
    print(len(spider_class.output))
