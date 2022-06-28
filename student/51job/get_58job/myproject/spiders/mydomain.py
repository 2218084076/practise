import scrapy

urls = []
for i in range(1, 3500):
    url = 'https://sh.58.com/job/pn%s/' % i
    urls.append(url)


class MydomainSpider(scrapy.Spider):
    name = '58job'
    # allowed_domains = ['mydomain.com']
    start_urls = urls

    def parse(self, response):
        pass
