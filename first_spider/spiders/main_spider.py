import scrapy, re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from first_spider.items import DoubanBookStatusItem


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
        # 长评入口
        # Rule(LinkExtractor(restrict_xpaths=('//*[@id="content"]/div/div[1]/div[3]/section/p/a'))),
        # 长评入口
        # Rule(LinkExtractor(restrict_xpaths=('//*[@id="content"]/div/div[1]/div[2]/span[4]/a'))),
        # 短评入口
        Rule(LinkExtractor(restrict_xpaths=(
            '//*[@id="content"]/div/div[1]/div[3]/p/a'))),
        # 短评翻页
        Rule(LinkExtractor(restrict_xpaths=(
            '//*[@id="content"]/div/div[1]/div/div[3]/ul/li[3]/a'),
            ), follow=True, callback='parse_item'),


    )

    def __init__(self):
        super().__init__()

    def key(self, stri):
        c = {}
        a = re.findall('(?<=<span class=").*?(?=" title)', stri)
        b = re.findall('(?<=<a href="https://www.douban.com/people/).*?(?=/">)', stri)
        d = re.findall('(?<=<span>).*?(?=</span>)', stri)
        if a == []:
            a.append('')
        c['user'] = b[0]
        c['star'] = a[0][18:-7]
        c['time'] = d[0]
        return c

    def parse_item(self, response):
        item = DoubanBookStatusItem()
        List = response.xpath('//*[@id="comments"]/ul/li').extract()   # 评分html组
        Book = response.xpath('//*[@id="content"]/div/div[2]/div/div/div').extract()
        item['comments'] = list(map(self.key, List))  # user和评分的字典

        item['name'] = re.findall('(?<=<span class="pl">书名:</span> ).*?(?=<br>)', Book[0])[0]
        item['writer'] = re.findall('(?<=<span class="pl">作者:</span> ).*?(?=<br>)', Book[0])[0]
        item['press'] = re.findall('(?<=<span class="pl">出版社:</span> ).*?(?=<br>)', Book[0])[0]
        item['year'] = re.findall('(?<=<span class="pl">出版年:</span> ).*?(?=<br>)', Book[0])[0]
        item['price'] = re.findall('(?<=<span class="pl">定价:</span> ).*?(?=<br>)', Book[0])[0]
        item['pages'] = re.findall('(?<=<span class="pl">页数:</span> ).*?(?=<br>)', Book[0])[0]

        yield item








