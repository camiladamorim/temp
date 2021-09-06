
BOT_NAME = 'temproject'

SPIDER_MODULES = ['temproject.spiders']
NEWSPIDER_MODULE = 'temproject.spiders'


ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'temproject.middlewares.CustomMiddleware': 543,
}

# ITEM_PIPELINES = {
#    'amazonbot.pipelines.AmazonbotPipeline': 300,
# }
