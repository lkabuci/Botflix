import scrapy
from rich.console import Console

console = Console()


# css selectors for the target data in https://torrentgalaxy.to/
MOVIES_TABLE = "div.panel-body.slidingDivf-7f2f71a3a90ac7c0cd3611e1ffaacd0e7c65d1c2 div.container-fluid div.tgxtable div.tgxtablerow.txlight"
MOVIE_TITLE = "div#click.tgxtablecell.clickable-row.click.textshadow.rounded.txlight div a.txlight b"
MOVIE_SIZE = (
    "div.tgxtablecell.collapsehide.rounded.txlight span.badge.badge-secondary.txlight"
)
LINK_SEED = "div.tgxtablecell.collapsehide.rounded.txlight span font b"
MOVIE_MAGNET_LINK = "div.tgxtablecell.collapsehide.rounded.txlight a"


class SearchedMoviesSpider(scrapy.Spider):
    output = []
    name = "topmovies"

    movie = "+".join(
        console.input("[bold]What movie are you looking for? [bold]").split(" ")
    )
    start_urls = [
        f"https://torrentgalaxy.to/torrents.php?c3=1&c46=1&c45=1&c42=1&c4=1&c1=1&search={movie}&sort=seeders&order=desc&lang=0&nox=2&nox=1#results"
    ]

    def parse(self, response):
        SearchedMoviesSpider.output = []

        for idx, movie in enumerate(response.css(MOVIES_TABLE), start=1):

            # get only 20 top movies by sorted by seeds/leechers
            if idx <= 20:

                items = {
                    "index": idx,
                    "title": movie.css(f"{MOVIE_TITLE}::text").getall()[0],
                }
                items["size"] = movie.css(f"{MOVIE_SIZE}::text").getall()[0]

                # [views, seeders, leechers]
                items["seeds"] = "/".join(movie.css(f"{LINK_SEED}::text").getall()[1:])
                items["views"] = movie.css(f"{LINK_SEED}::text").getall()[0]

                # use [0]: to access to the download .torrent
                # use [1]: to get the magnet link
                items["link"] = movie.css(f"{MOVIE_MAGNET_LINK}::attr(href)").getall()[
                    1
                ]

                SearchedMoviesSpider.output.append(items)
                yield items
