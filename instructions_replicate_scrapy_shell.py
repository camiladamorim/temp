
#scrapy shell 'https://www.youtube.com/results?search_query=tempest&sp=EgIQAg%253D%253D'


import re

general_response=response.xpath('//*/text()').extract()

for i in range(len(general_response)):
    if i == 40:
        str_channels = general_response[i]
        list_all_channels = re.split('channelRenderer', str_channels)


a1=list_all_channels[5]

a2 = re.split('\,', a1)

for i in a2:
    if "descriptionSnippet" in i:
        descricao = re.split("(\"text\"\:)", item)[2]