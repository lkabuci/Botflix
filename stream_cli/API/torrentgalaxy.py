import scrapy
from scrapy.crawler import CrawlerProcess
from rich.console import Console

console = Console()

# css selectors for the target data in https://torrentgalaxy.to/
MOVIES = "div.tgxtable div.tgxtablerow"
TITLE = "div.textshadow div a.txlight b::text"
SIZE = "div span.badge::text"
SEEDS = "div span[title='Seeders/Leechers'] font b::text"
VIEWS = "div span[title='Views'] font b::text"
LINKS = "div[style='text-align:center;width:52px;padding-bottom:0px;padding-top:5px;'] a:nth-child(2)::attr(href)"


class TopMoviesSpider(scrapy.Spider):
    name = "topmovies"
    start_urls = ["https://torrentgalaxy.to/"]

    output = []

    def parse(self, response):
        movies = response.css(MOVIES)
        for idx, movie in enumerate(movies, start=1):

            # Get only the top 10 movies!
            if idx <= 10:
                items = {
                    "index": idx,
                    "title": movie.css(TITLE).get(),
                    "size": movie.css(SIZE).get(),
                    "seeds": "/".join(movie.css(SEEDS).getall()[:2]),
                    "views": movie.css(VIEWS).get(),
                    "link": movie.css(LINKS).get(),
                }
                TopMoviesSpider.output.append(items)
                yield items


class MoviesSpider(scrapy.Spider):
    output = []
    name = "topmovies"

    movie = "+".join(
        console.input("[bold]What movie are you looking for? [bold]").split(" ")
    )
    start_urls = [
        f"https://torrentgalaxy.to/torrents.php?c3=1&c46=1&c45=1&c42=1&c4=1&c1=1&search={movie}&sort=seeders&order=desc&lang=0&nox=2&nox=1#results"
    ]

    def parse(self, response):
        movies = response.css(MOVIES)
        movies = response.css(MOVIES)
        for idx, movie in enumerate(movies, start=1):

            # Get only the top 20 movies in search
            if idx <= 20:
                items = {
                    "index": idx,
                    "title": movie.css(TITLE).get(),
                    "size": movie.css(SIZE).get(),
                    "seeds": "/".join(movie.css(SEEDS).getall()[:2]),
                    "views": movie.css(VIEWS).get(),
                    "link": movie.css(LINKS).get(),
                }
                MoviesSpider.output.append(items)
                yield items


class SeriesSpider(scrapy.Spider):

    output = []
    name = "serie"

    serie = "+".join(
        console.input("[bold]What serie are you looking for? [bold]").split(" ")
    )
    start_urls = [
        f"https://torrentgalaxy.to/torrents.php?c41=1&c5=1&c6=1&search={serie}&lang=0&nox=1&sort=seeders&order=desc"
    ]

    def parse(self, response):
        for idx, movie in enumerate(response.css(MOVIES), start=1):

            # get only 20 top result by sorted by seeds/leechers
            if idx <= 20:

                items = {
                    "index": idx,
                    "title": movie.css(TITLE).get(),
                    "size": movie.css(SIZE).get(),
                    "seeds": "/".join(movie.css(SEEDS).getall()[:2]),
                    "views": movie.css(VIEWS).get(),
                    "link": movie.css(LINKS).get(),
                }

                SeriesSpider.output.append(items)
                yield items
