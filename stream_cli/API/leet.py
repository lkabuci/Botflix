import scrapy
from scrapy.crawler import CrawlerProcess

from typing import Optional

MOVIES = "tbody tr"
MOVIE_INFO = "div.torrent-detail-page"
TITLE = "div h1::text"
SIZE = "div.no-top-radius div.clearfix ul.list li:nth-child(4) span::text"
SEEDS = "div.no-top-radius div.clearfix ul.list:nth-child(3) li:nth-child(4) span::text"
LEECHES = "div.no-top-radius div.clearfix ul.list:nth-child(3) li:nth-child(5) span::text"
VIEWS = "div.no-top-radius div.clearfix ul.list:nth-child(3) li span::text"
DOMAIN = "https://1337x.to"
PAGE_INFO = "td a:nth-child(2)::attr(href)"
MAGNET = "div.no-top-radius div.clearfix ul li a::attr(href)"


# I need to go inside the (MOVIEPAGE) and get the link

def leet(name: Optional[str], category: str, limit_results: int):

    def _set_category() -> str:
        """return the target url"""

        converted_name = "%20".join(name.split()) + "%207"

        if category == "movie":
            return f"https://1337x.to/category-search/{converted_name}%207/Movies/1/"
        elif category == "serie":
            return f"https://1337x.to/category-search/{converted_name}%207/TV/1/"
        elif category == "top":
            return "https://1337x.to/popular-movies"

    def _set_limit() -> int:
        """return the limit of results as int"""

        return 27 if limit_results > 27 else limit_results

    class _Leet(scrapy.Spider):

        output = []
        idx = 1
        name = "leet"
        url = _set_category()

        start_urls = [url]

        def parse(self, response):
            limit = _set_limit()
            movies = response.css(MOVIES)
            for idx, movie in enumerate(movies, start=1):
                if idx <= limit:
                    page_info = DOMAIN + movie.css("td a:nth-child(2)::attr(href)").get()
                    yield response.follow(page_info, callback=self.parse_magnet_link)
            
        def parse_magnet_link(self, response):

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

# This is just for testing the spider manually
if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "LOG_LEVEL": "ERROR",
            "USER_AGENT": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        }
    )

    spider_class = leet(category="top", name="peaky blinders", limit_results=55)
    process.crawl(spider_class)
    process.start()
    ouut = spider_class.output
    
    print(ouut)
    print(len(ouut))
