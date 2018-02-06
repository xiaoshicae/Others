# -*- coding: utf-8 -*-

# Scrapy settings for jianshu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jianshu'

SPIDER_MODULES = ['jianshu.spiders']
NEWSPIDER_MODULE = 'jianshu.spiders'

# 采用scrapy_redis调度
DUPEFILTER_CLASS = "jianshu.scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = 'jianshu.scrapy_redis.scheduler.Scheduler'
SCHEDULER_QUEUE_CLASS = 'jianshu.scrapy_redis.queue.SpiderPriorityQueue'
SCHEDULER_PERSIST = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'jianshu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {'Accept': 'application/json',
                           'Accept-Encoding': 'gzip, deflate, br',
                           'Accept-Language': 'zh-CN,zh;q=0.9',
                           'Connection': 'keep-alive',
                           'Content-Length': '0',
                           'Cookie': 'remember_user_token=W1s3MzQ1MDIzXSwiJDJhJDEwJGY0UjV6TExLczZIVXVFV3VDaVlqaU8iLCIxNTE2OTM3NDE3LjIzMjA1NzYiXQ%3D%3D--110dc84d34b53ad69d27d2255464f3d1f8e2463d; '
                                     'read_mode=day; default_font=font2; locale=zh-CN; '
                                     '_m7e_session=9e30ec7ba5252443a66f13487fc5ddc3; '
                                     'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1517385521,1517406920,1517446551,1517446591; '
                                     'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%227345023%22%2C%22%24device_id%22%3A%221613083ab8cab-0517b183f72795-3c60460e-1247616-1613083ab8d372%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-trending%22%7D%2C%22first_id%22%3A%221613083ab8cab-0517b183f72795-3c60460e-1247616-1613083ab8d372%22%7D; '
                                     'Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1517455695',
                           'Host': 'www.jianshu.com',
                           'Origin': 'https://www.jianshu.com',
                           'Referer': 'https://www.jianshu.com/search?q=%E6%97%85%E8%A1%8C%E9%9D%92%E8%9B%99&page=1&type=note',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
                           'X-CSRF-Token': 'qwU7K3IFq+zu56eDz2vGy0rW7clBGWGGIMrg7ezidwH0OZFPTu8jjmbfagxlruO2VAx7ORUOMQVYxOB1C6AHKw=='}
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'jianshu.middlewares.JianshuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'jianshu.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jianshu.pipelines.RedisPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# redis config
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
