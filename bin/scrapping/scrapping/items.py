import scrapy


class ScrappingItem(scrapy.Item):
    index = scrapy.Field()
    title = scrapy.Field()
    size = scrapy.Field()
    seeds = scrapy.Field()
    views = scrapy.Field()
    link = scrapy.Field()