import scrapy
from ..items import ZolItem
from scrapy_redis.spiders import RedisSpider
from scrapy.loader import ItemLoader


class getZOLSpider(scrapy.Spider):
    name = "get_zol"
    allowed_domains = ["zol.com.cn"]
    domain = 'https://detail.zol.com.cn'
    start_urls = ["https://detail.zol.com.cn/cell_phone_advSearch/subcate57_1_g0-g2000-g4600-g7600_1_1_0_1.html#showc"]
    # redis_key = "get_zol:start_urls"

    def parse(self, response):
        # 示例: https://detail.zol.com.cn/cell_phone_advSearch/subcate57_1_g0-g2000-g4600-g7600_1_1__1.html#showc
        product_item = response.xpath("//*[@id='result_box']/div[2]/ul/li//a[text()='更多参数>>']/@href")
        for i in product_item:
            #详情页url
            detail_url = 'https://detail.zol.com.cn/{}'.format(i)
            yield scrapy.Request(url=detail_url, callback=self.parse_detail)

        # next_page = response.xpath("//a[text()='下一页>']/@href").extract_first()
        # if next_page:
        #     next_page_url = 'https://detail.zol.com.cn/{}'.format(next_page)
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detail(self, response):
        """解析详情页"""
        # 示例:https://detail.zol.com.cn/2105/2104769/param.shtml
        l = ItemLoader(item=ZolItem(), response=response)
        l.add_value("id", response.url.split("/")[-2])
        l.add_xpath("品牌", "//div[@class='detailed-parameters']/table//th//text()")
        product_keys = set(response.xpath("//div[@class='detailed-parameters']/table//th//text()").extract())
        data = {}
        for k in product_keys:
            if k.startswith("\r\n"):
                continue
            data[k] = response.xpath("//tr[th/span[text()='{}']]/td/span//text()".format(k)).extract()
            l.add_value(k, data[k])
        print(data)

        yield l.load_item()
