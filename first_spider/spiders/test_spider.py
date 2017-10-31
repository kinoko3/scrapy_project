import scrapy
from ..items import FirstSpiderItem


class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://www.bilibili.com/'
    ]

    def parse(self, response):
        # 返回一个list
        a = response.xpath('//*[@id="primary_menu"]/ul/li/a/div/text()').extract()
        #
        item = FirstSpiderItem()
        item['title'] = a  # 返回一个字典，和BSON的格式相符
        # self.logger.warning(item)
        return item


