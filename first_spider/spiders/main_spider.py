import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DoubanBookStatusItem


class MainDoubanBookSpider(CrawlSpider):
    name = "DoubanBook"
    start_urls = [
        'https://book.douban.com/latest'
    ]
    rules = (

        Rule(LinkExtractor(allow=('/subject/\d+')), callback='parse_item'),  # 回调函数返回一个response

    )

    def parse_item(self, response):
        self.logger.info("%s" % response.url)
        a = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()
        self.logger.info(a)

