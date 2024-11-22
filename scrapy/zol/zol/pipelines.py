# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis
import json


class ZolPipeline:
    def process_item(self, item, spider):
        return item


class RedisPipeline:
    def __init__(self, redis_url, redis_db, redis_key):
        self.redis_url = redis_url
        self.redis_db = redis_db
        self.redis_key = redis_key
        self.redis = redis.StrictRedis.from_url(redis_url, db=redis_db)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # 从 Scrapy 设置中获取 Redis 配置
        redis_url = crawler.settings.get('REDIS_URL')
        redis_db = crawler.settings.get('REDIS_DB', 0)
        redis_key = crawler.settings.get('REDIS_KEY', 'scrapy:items')
        return cls(redis_url, redis_db, redis_key)

    def process_item(self, item, spider):
        # 将每个抓取到的数据转换成 JSON 格式并存储到 Redis
        self.redis.lpush(self.redis_key, json.dumps(item))
        return item
