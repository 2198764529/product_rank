# Scrapy settings for zol project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zol"

SPIDER_MODULES = ["zol.spiders"]
NEWSPIDER_MODULE = "zol.spiders"

# settings.py

#
# # Redis 配置
# REDIS_URL = 'redis://localhost:6379'  # Redis 服务地址
# REDIS_DB = 0  # Redis 数据库
# REDIS_KEY = 'scrapy:items'  # 存储数据的 Redis 键
#
# # 启用自定义的 RedisPipeline
# ITEM_PIPELINES = {
#    'zol.pipelines.RedisPipeline': 1,
# }

# 其他设置
# DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'  # 去重
# SCHEDULER_PERSIST = True  # 保证任务不丢失

# 只在使用SpiderQueue或者SpiderStack是有效的参数，指定爬虫关闭的最大间隔时间
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中，供后面的分布式处理item
# 这个已经由 scrapy-redis 实现，不需要我们写代码


# 指定redis数据库的连接参数
# REDIS_PASS是我自己加上的redis连接密码（默认不做）
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
# REDIS_PASS = 'redisP@ssw0rd'

# settings.py
#
# # Redis 配置
# REDIS_URL = 'redis://localhost:6379'  # Redis 服务地址
# REDIS_DB = 0  # Redis 数据库
# REDIS_KEY = 'scrapy:items'  # 存储数据的 Redis 键
#
# # 启用自定义的 RedisPipeline
# ITEM_PIPELINES = {
#    'zol.pipelines.RedisPipeline': 1,
# }
#
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#

# myproject/settings.py
FEEDS = {
    'output.json': {'format': 'json', 'encoding': 'utf8', 'overwrite': True},
}
# 其他设置
# DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'  # 去重
# SCHEDULER = 'scrapy.schedulers.Scheduler'  # 调度器
# SCHEDULER_PERSIST = True  # 保证任务不丢失

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (defauslt: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zol.middlewares.ZolSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "zol.middlewares.ZolDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zol.pipelines.ZolPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"



# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
DOWNLOAD_DELAY = 1.2  # 每次请求之间等待 2 秒
