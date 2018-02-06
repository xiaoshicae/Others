# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import math

import redis
from urllib.parse import quote


class JianshuPipeline(object):
    def process_item(self, item, spider):
        return item


class RedisPipeline:
    queue = 'PageSpider:start_urls'

    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('REDIS_HOST'),
            port=crawler.settings.get('REDIS_PORT', 6379)
        )

    def open_spider(self, spider):
        self.client = redis.Redis(host=self.host, port=self.port)

    def close_spider(self, spider):
        self.client.client_kill('ip:port')

    def process_item(self, item, spider):
        slug = item['slug']
        url = 'https://www.jianshu.com/p/%s' % slug
        self.lpush(url)
        return item

    def lpush(self, value):
        self.client.lpush(self.queue, value)

