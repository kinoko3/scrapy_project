import scrapy, re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from first_spider.items import DoubanBookStatusItem


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
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="subject_list"]/div[2]/span[4]/a'), deny=('/tag/日本文学\?start=40\&type=S'))),
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="subject_list"]/ul'),
                           deny=('/\d+/.+')
                           ), callback='parse_item'),

    )

    def parse_item(self, response):
        item = DoubanBookStatusItem()
        name = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()[0]
        writer = response.xpath('//*[@id="info"]/a[1]/text()').extract()[0]
        writer = re.sub('\s+', '', writer)
        item['name'] = name  # 书名
        item['writer'] = writer   # 作者
        item['press'] = response.xpath('//*[@id="info"]').re('(?<=出版社:</span> ).*?(?=<br>)')[0]    # 出版社
        item['year'] = response.xpath('//*[@id="info"]').re('(?<=出版年:</span> ).*?(?=<br>)')[0]   # 出版年份
        item['price'] = response.xpath('//*[@id="info"]').re('(?<=定价:</span> ).*?(?=<br>)')[0]   # 价格
        item['pages'] = response.xpath('//*[@id="info"]').re('(?<=页数:</span> ).*?(?=<br>)')[0]   # 页数
        item['grade'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract()[0]  # 评分
        self.logger.warning(response.url)
        self.logger.warning(name)
        yield item


