import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DoubanBookStatusItem


class MainDoubanBookSpider(CrawlSpider):
    name = "DoubanBook"
    allowed_domains = ["book.douban.com"]
    start_urls = [
        'https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6?type=S'
    ]
    rules = (
        # restrict_xpaths=装着link的一个标签树，不需要精准,对一页中的全部书籍的链接进行回调分析
        # Rule(LinkExtractor(restrict_xpaths=('//*[@id="subject_list"]/ul'),
                           # deny=('/\d+/.+')
                           # ), callback='parse_item'),  # 回调函数返回一个response
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="subject_list"]/div[2]/span[4]/a'), deny=('/tag/日本文学\?start=200\&type=S'))),
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="subject_list"]/ul'),
                           deny=('/\d+/.+')
                           ), callback='parse_item'),

    )

    def parse_item(self, response):

        a = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()
        self.logger.warning(response.url)
        self.logger.warning(a)



