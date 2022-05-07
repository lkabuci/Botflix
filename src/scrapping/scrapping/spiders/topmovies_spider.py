import scrapy

# css selectors for the target data in https://torrentgalaxy.to/
MOVIES_TABLE = "div.slidingDivb-b6a23717a851a6fc9b4c2e09f0073f0857d7f4d8 div.container-fluid div.tgxtable div.tgxtablerow.txlight"
MOVIE_TITLE = "div.tgxtablecell a.txlight b"
MOVIE_SIZE = "span.badge.badge-secondary.txlight"
MOVIE_MAGNET_LINK = "div.tgxtablecell.collapsehide.rounded.txlight a"
LINK_SEED = "div.tgxtablecell.collapsehide.rounded.txlight span font b"


class TopMoviesSpider(scrapy.Spider):
    output = []
    name = "topmovies"
    start_urls = ["https://torrentgalaxy.to/"]

    def parse(self, response):
        TopMoviesSpider.output = []
        for idx, movie in enumerate(response.css(MOVIES_TABLE), start=1):
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
            items["link"] = movie.css(f"{MOVIE_MAGNET_LINK}::attr(href)").getall()[1]

            TopMoviesSpider.output.append(items)
            yield items
