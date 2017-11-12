import scrapy
from first_spider.items import TagType


class BookTag(scrapy.Spider):
    name = 'tag'
    allowed_domains = ["book.douban.com"]
    start_urls = [
        'https://book.douban.com/tag/?view=type'
    ]

    def parse(self, response):
        items = TagType()
        items['literature'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/div[1]/table/tbody/tr/td/a/@href').extract()
        items['popular'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/div[2]/table/tbody/tr/td/a/@href').extract()
        items['culture'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/div[3]/table/tbody/tr/td/a/@href').extract()
        items['life'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/div[4]/table/tbody/tr/td/a/@href').extract()
        items['manage'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/div[5]/table/tbody/tr/td/a/@href').extract()
        items['science'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/div[6]/table/tbody/tr/td/a/@href').extract()
        return items