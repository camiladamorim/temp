
import scrapy
# from ...items import TemprojectItem


class TempSpider(scrapy.Spider):

    name = 'temp'
    allowed_domains = ['youtube.com']
    start_urls = ['https://www.youtube.com/results?search_query=tempest&sp=EgIQAg%253D%253D'] #so o 1 termo


    # lista_canais = ['tempest', 'youtube', 'estrela']
    # name = 'temp'
    # allowed_domains = ['youtube.com']
    # for item in lista_canais:
    #     url='https://www.youtube.com/results?search_query='+item+'&sp=EgIQAg%253D%253D'
    #     start_urls = [url]




    def parse(self, response):
        
        all_channels = response.xpath('//*/text()').extract()
        #response.xpath('//*/text()')[41].extract()
        #response.xpath('//*/text()')[40].extract()

        yield {
            'all_channels': all_channels
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
