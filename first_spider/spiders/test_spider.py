import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://www.bilibili.com/'
    ]

    def parse(self, response):
        for a in response.xpath('//*[@id="primary_menu"]/ul/li').extract():
            self.logger.warning(a)
