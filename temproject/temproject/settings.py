
BOT_NAME = 'temproject'

SPIDER_MODULES = ['temproject.spiders']
NEWSPIDER_MODULE = 'temproject.spiders'


ROBOTSTXT_OBEY = True


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}


ITEM_PIPELINES = {
   'amazonbot.pipelines.AmazonbotPipeline': 300,
}
