import scrapy
from rich.console import Console

console = Console()

MOVIES = "div.tgxtable div.tgxtablerow"
TITLE = "div.textshadow div a.txlight b::text"
SIZE = "div span.badge::text"
SEEDS = "div span[title='Seeders/Leechers'] font b::text"
VIEWS = "div span[title='Views'] font b::text"
LINKS = "div[style='text-align:center;width:52px;padding-bottom:0px;padding-top:5px;'] a:nth-child(2)::attr(href)"


class SeriesSpider(scrapy.Spider):
    output = []
    name = "serie"

    movie = "+".join(
        console.input("[bold]What serie are you looking for? [bold]").split(" ")
    )
    start_urls = [
        f"https://torrentgalaxy.to/torrents.php?c41=1&c5=1&c6=1&search={movie}&lang=0&nox=1&sort=seeders&order=desc"
    ]

    def parse(self, response):
        SeriesSpider.output = []

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
