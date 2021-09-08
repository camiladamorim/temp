
import scrapy
import re
# from ...items import TemprojectItem


class TempSpider(scrapy.Spider):

        name = 'temp'
        allowed_domains = ['youtube.com']

        start_urls=[]
        keywords = ['tempest', 'youtube', 'estrela']
        for keyword in keywords:
            url='https://www.youtube.com/results?search_query='+keyword+'&sp=EgIQAg%253D%253D'
            start_urls.append(url)


        def parse(self, response):

                general_response = response.xpath('//*/text()').extract()  

                for i in range(len(general_response)):
                        if i==40:
                                str_channels=general_response[i]
                                list_channels=re.split('channelRenderer', str_channels)
                                list_channel_1=re.split('\,', list_channels[1])
                                for element in list_channel_1:
                                        if "shortBylineText" in element:
                                                titulo =re.split("(\"text\"\:)", element)[2]
                                                
                                        if "descriptionSnippet" in element: #
                                                descricao =re.split("(\"text\"\:)", element)[2]

                                        if "url" in element: 
                                                url = re.split("(\"url\"\:)", element)[2]

                                        if "thumbnails" in element:
                                                img = re.split("(\"url\"\:)", element)[2]

                                        if "searchEndpoint" in element:
                                                query = str(re.split("^query(.*)", element)[0])
                                                if "query" in query:
                                                        query = re.split("query\"\:\"", query)[1]

                                        if "channelId" in element:
                                                id_ = str(re.split("^channelId(.*)", element)[0])
                                                if "channelId" in id_:
                                                        id_ = re.split("channelId\"\:\"", id_)[1]
                                

                yield {
                        'titulo': titulo,
                        'descricao': descricao,
                        'url': url,
                        'img': img,
                        'query': query,
                        'id_': id_
                }


        # #mod
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback = self.parse)
