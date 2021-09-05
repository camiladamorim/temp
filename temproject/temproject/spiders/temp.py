

# lista = [tempest, youtube, estrela]

# for item in lista:
#     print("item")


import scrapy
from ...items import TemprojectItem


class TempSpider(scrapy.Spider):

    name = 'temp'
    allowed_domains = ['youtube.com']
    start_urls = ['https://www.youtube.com/']



    

    def parse(self, response):
        #title = response.css('#product-widget-title').extract()
        items = TemprojectItem()
        # title = response.css('.text::text').extract()
        all_div_quotes = response.css('div.quote')


        for div_quote in all_div_quotes:

            titulo = div_quote.css('span.text::text').extract() #nome do canal
            descricao = div_quote.css('span.text::text').extract() #descrição do canal
            # url = div_quote.css('span.text::text').extract() #url do canal
            # img = div_quote.css('span.text::text').extract() #base64 da imagem de perfil do canal
            # query = div_quote.css('span.text::text').extract() #a palavra chave utilizada na busca que encontrou o canal

            # id_ = div_quote.css('span.text::text').extract() #um identificador único para esse canal (sugestão, existe um campo "channelId" dentro da resposta do youtube)
            # use o href por ex:class="channel-link yt-simple-endpoint style-scope ytd-channel-renderer"



                    
            items['titulo'] = titulo
            items['descricao'] = descricao
            # items['url'] = url
            # items['img'] = img
            # items['query'] = query
            # items['id'] = id_

            yield items
        #mod
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)










# #nome do canal
# titulo =  

# #descrição do canal
# descricao =  

# #url do canal
# url =   

# #base64 da imagem de perfil do canal
# img =   

# #a palavra chave utilizada na busca que encontrou o canal
# query =   

# #um identificador único para esse canal (sugestão, existe um campo "channelId" dentro da resposta do youtube)
# id =   
