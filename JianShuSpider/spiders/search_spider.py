# --*-- coding: utf-8 --*--
# --------------------------------------------------------------------------------
#  Description:
#       search_spider负责将搜索结果扔进redis队列,提供给page_spider消费
#       两步爬虫分离,实现分布式,弹性扩展
#  DATE:
#       2018/02/01
#  BY:
#       xiaoshicae
# --------------------------------------------------------------------------------
import re
import json

from scrapy.http import Request

from jianshu.scrapy_redis.spiders import RedisSpider
from jianshu.items import PageItem


class SearchSpider(RedisSpider):
    name = "SearchSpider"
    redis_key = "%s:start_urls" % name

    # 流程 redis_start_urls -> start_requests -> next_requests -> make_requests_from_url -> parse
    # 改写start_requests会影响next_requests(向redis请求任务),因此改写make_requests_from_url,修改获取url后的处理逻辑
    # dont_filter=False就会进入dupefilter进行去重判断
    def make_requests_from_url(self, url):
        # return Request(url, dont_filter=False)
        return Request(url, method='POST', dont_filter=True)

    def parse(self, response):
        item = PageItem()
        json_resp = json.loads(response.text)
        total_page = json_resp.get('total_count', 1)
        search_word = json_resp.get('q', '')
        json_resp = json.loads(response.text)

        entries = json_resp.get('entries', [])
        for entry in entries:
            item['slug'] = entry.get('slug', '')
            yield item

        for i in range(2, total_page + 1):
            url = 'https://www.jianshu.com/search/do?q=%s&type=note&page=%d&order_by=default' % (search_word, i)
            yield Request(url, method='POST', callback=self.parse_entries)

    def parse_entries(self, response):
        item = PageItem()
        json_resp = json.loads(response.text)

        entries = json_resp.get('entries', [])
        for entry in entries:
            item['slug'] = entry.get('slug', '')
            yield item
