
import scrapy
import re
from ..items import TemprojectItem

class TempSpider(scrapy.Spider):

        name = 'temp'
        allowed_domains = ['youtube.com']

        start_urls=[]
        keywords = ['tempest', 'youtube', 'estrela']
        for keyword in keywords:
            url='https://www.youtube.com/results?search_query='+keyword+'&sp=EgIQAg%253D%253D'
            start_urls.append(url)
        

        def parse(self, response):
                items = TemprojectItem()
                general_response = response.xpath('//*/text()').extract()  

                for i in range(len(general_response)):
                        if i == 40:
                                str_channels = general_response[i]
                                list_all_channels = re.split('channelRenderer', str_channels) 

                placeholder=[]
                titulo, descricao, url, img, query, id_= '','','','','',''      
                for channel in list_all_channels:
                        items_inside_each_channel = re.split('\,', channel)
                        for item in items_inside_each_channel:
                                if "shortBylineText" in item:
                                        titulo = re.split("(\"text\"\:)", item)[2]
                                        
                                if "descriptionSnippet" in item: #
                                        descricao = re.split("(\"text\"\:)", item)[2]

                                if "url" in item: 
                                        url = re.split("(\"url\"\:)", item)[2]

                                if "thumbnails" in item:
                                        img = re.split("(\"url\"\:)", item)[2]

                                if "searchEndpoint" in item:
                                        query = str(re.split("^query(.*)", item)[0])
                                        if "query" in query:
                                                query = re.split("query\"\:\"", query)[1]

                                if "channelId" in item:
                                        id_ = str(re.split("^channelId(.*)", item)[0])
                                        if "channelId" in id_:
                                                id_ = re.split("channelId\"\:\"", id_)[1]
                        

                        items['titulo'] = titulo
                        items['descricao'] = descricao
                        items['url'] = url
                        items['img'] = img
                        items['query'] = query
                        items['id_'] = id_


                        yield items