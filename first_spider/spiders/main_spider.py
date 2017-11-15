import scrapy, re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from first_spider.items import Comments


class MainDoubanBookSpider(CrawlSpider):
    name = "DoubanBook"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6"]
    rules = (
        # restrict_xpaths=装着link的一个标签树，不需要精准,对一页中的全部书籍的链接进行回调分析
        # Rule(LinkExtractor(restrict_xpaths=('//*[@id="subject_list"]/ul'),
        # deny=('/\d+/.+')
        # ), callback='parse_item'),  # 回调函数返回一个response
        # 第一规则，标签翻页
        Rule(LinkExtractor(restrict_xpaths=(
            '//*[@id="subject_list"]/div[2]/span[4]/a'), deny=(
            '/tag/\w+\?start=20\&type=T'))),
        Rule(LinkExtractor(restrict_xpaths=(
            '//*[@id="subject_list"]/ul'),
            deny=(
                '/\d+/.+')
        ),),
        Rule(LinkExtractor(restrict_xpaths=(
            '//*[@id="content"]/div/div[1]/div[3]/p/a'),
        ), ),
        Rule(LinkExtractor(restrict_xpaths=(
            '//*[@id="content"]/div/div[1]/div/div[3]/ul/li[3]/a')),
            callback='parse_item', follow=True
        ),

    )

    def __init__(self):
        super().__init__()

    def parse_item(self, response):
        item = Comments()
        a = response.xpath('//*[@id="comments"]/ul/li/div[1]/a/@href').extract()



        self.logger.warning(response.url)









