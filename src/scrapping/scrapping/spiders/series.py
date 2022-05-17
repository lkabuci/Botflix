import scrapy
from rich.console import Console

console = Console()


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

        for idx, movie in enumerate(response.css("div.tgxtable div.tgxtablerow"), start=1):

            # get only 20 top result by sorted by seeds/leechers
            if idx <= 20:

                items = {
                    "index": idx,
                    "title": movie.css("div.textshadow div a.txlight b::text").get(),
                    "size": movie.css("div span.badge::text").get(),
                    "seeds": "/".join(movie.css("div span[title='Seeders/Leechers'] font b::text").getall()[:2]),
                    "views": movie.css("div span[title='Views'] font b::text").get(),
                    "link": movie.css("div[style='text-align:center;width:52px;padding-bottom:0px;padding-top:5px;'] a:nth-child(2)::attr(href)").get(),
                }

                SeriesSpider.output.append(items)
