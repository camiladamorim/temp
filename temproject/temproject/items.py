
import scrapy


class TemprojectItem(scrapy.Item):
    titulo = scrapy.Field()
    descricao = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
    query = scrapy.Field()
    id_ = scrapy.Field()



    