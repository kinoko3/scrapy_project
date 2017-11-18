# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo


class MongoPipline(object):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_server, port, db_name):
        self.mongo_server = mongo_server
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGODB_SERVER'),
            port=crawler.settings.get('MONGODB_PORT'),
            db_name=crawler.settings.get('MONGODB_DB'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_server, self.port)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # self.db[self.collection_name].insert_one(dict(item))
        self.db[self.collection_name].update({
                'name': item['name'],
                'pages': item['pages'],
                'year': item['year'],
                'writer': item['writer'],
                'price': item['price']
            }, {
                '$push': {
                    'comments': {
                        '$each': item['comments']
                    }
                },
            },
                upsert=True)
        return item