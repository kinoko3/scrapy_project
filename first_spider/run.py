import json, configparser
from first_spider.spiders.main_spider import MainDoubanBookSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


# 返回启动链接，一个链接一个爬虫进程
def urls():
    with open('start_url.json', 'r') as f:
        url = json.load(f)['url']
        return url


url_list = urls()

config = configparser.ConfigParser()    #读取配置


settings = get_project_settings()   # 获取当前目录下的settings的配置

configure_logging(settings)     # 日志等级获取
runner = CrawlerRunner(settings)    #

runner.crawl(MainDoubanBookSpider())

d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()