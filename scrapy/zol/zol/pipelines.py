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
    def __init__(self, host, port, db):
        self.redis_host = host
        self.redis_port = port
        self.redis_db = db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('REDIS_HOST', 'localhost'),
            port=crawler.settings.get('REDIS_PORT', 6379),
            db=crawler.settings.get('REDIS_DB', 0),
        )

    def open_spider(self, spider):
        # 在爬虫启动时建立 Redis 连接
        self.redis_conn = redis.StrictRedis(
            host=self.redis_host,
            port=self.redis_port,
            db=self.redis_db,
            decode_responses=True  # 确保字符串不需要二次解码
        )

    def close_spider(self, spider):
        # 在爬虫关闭时断开 Redis 连接
        self.redis_conn.close()

    def process_item(self, item, spider):
        # 将 item 转换为 JSON 格式并存储到 Redis
        self.redis_conn.rpush('scrapy_items', json.dumps(dict(item), ensure_ascii=False))
        return item
