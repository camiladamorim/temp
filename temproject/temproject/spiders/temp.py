
import scrapy
import re
# from ...items import TemprojectItem


class TempSpider(scrapy.Spider):

    name = 'temp'
    allowed_domains = ['youtube.com']
    start_urls = ['https://www.youtube.com/results?search_query=tempest&sp=EgIQAg%253D%253D'] #so o 1 termo


    # lista_canais = ['tempest', 'youtube', 'estrela']
    # for item in lista_canais:
    #     url='https://www.youtube.com/results?search_query='+item+'&sp=EgIQAg%253D%253D'
    #     start_urls = [url]




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

####################################################################

        # for div_quote in all_channels:

        #     titulo = div_quote.css('span.text::text').extract() #nome do canal
        #     descricao = div_quote.css('span.text::text').extract() #descrição do canal
        #     # url = div_quote.css('span.text::text').extract() #url do canal
        #     # img = div_quote.css('span.text::text').extract() #base64 da imagem de perfil do canal
        #     # query = div_quote.css('span.text::text').extract() #a palavra chave utilizada na busca que encontrou o canal
        #     # id_ = div_quote.css('span.text::text').extract() #um identificador único para esse canal (sugestão, existe um campo "channelId" dentro da resposta do youtube)
        #     # use o href por ex:class="channel-link yt-simple-endpoint style-scope ytd-channel-renderer"


        #     items['titulo'] = titulo
        #     items['descricao'] = descricao
        #     # items['url'] = url
        #     # items['img'] = img
        #     # items['query'] = query
        #     # items['id'] = id_

        #     yield items


        # #mod
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback = self.parse)
