import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['get_cdf.cn']
    start_urls = ['http://get_cdf.cn/']

    def parse(self, response):
        pass
