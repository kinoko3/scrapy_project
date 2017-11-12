# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    pass


class DoubanBookStatusItem(scrapy.Item):
    # 豆瓣读书暂定书本状态字段
    name = scrapy.Field()  # 书名
    writer = scrapy.Field()  # 作者
    press = scrapy.Field()  # 出版社
    year = scrapy.Field()  # 出版年份
    price = scrapy.Field()  # 价格
    pages = scrapy.Field()  # 页数
    # 下面是评分
    grade = scrapy.Field()


class TagType(scrapy.Item):
    literature = scrapy.Field()   # 文学
    popular = scrapy.Field()  # 流行
    culture = scrapy.Field()  # 文化
    life = scrapy.Field()  # 生活
    manage = scrapy.Field()  # 经管
    science = scrapy.Field()  # 科技
