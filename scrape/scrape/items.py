# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class movie(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pub_time = scrapy.Field()
    score = scrapy.Field()
    create_time = scrapy.Field()
    page_url = scrapy.Field()