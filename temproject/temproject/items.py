# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TemprojectItem(scrapy.Item):
    title = scrapy.Field()
    descricao = scrapy.Field()
    # url = scrapy.Field()
    # img = scrapy.Field()
    # query = scrapy.Field()
    # id_ = scrapy.Field()