import re

import scrapy
from scrapy_splash import SplashRequest


class TestingSpider(scrapy.Spider):
    name = "test_spider"
    allowed_domains = ["lianjia.com"]
    start_urls = ['https://cd.fang.lianjia.com/loupan/p_sdjzabhoq/']

    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse,
                            args={
                                # optional; parameters passed to Splash HTTP API
                                'wait': 20,

                                # 'url' is prefilled from request url
                                # 'http_method' is set to 'POST' for POST requests
                                # 'body' is set to request body for POST requests
                            })

    def parse(self, response):
        layout_list = []
        layout_dict = {}

        layout_ul_s = response.xpath('//ul[@class="clear house-det"]')
        for layout_ul in layout_ul_s:
            img_src = layout_ul.xpath('child::*/img/@src').extract_first()
            img_src = re.sub(r'\d+?x\d*', '1000x', img_src)
            layout_dict['img_src'] = img_src
            layout_dict['layout_type_name'] = layout_ul.xpath('child::*/span/text()').extract_first()

            info_li = layout_ul.xpath('li[@class="info-li"]')
            p1 = info_li.xpath('p[@class="p1"]')
            layout_dict['layout_type'] = p1.xpath('text()').extract_first()
            layout_dict['construction_area'] = p1.xpath('span[not(@class)]/text()').extract_first()
            layout_dict['sales_status'] = p1.xpath('span[contains(@class,"p1-state")]/text()').extract_first()

            p2 = info_li.xpath('p[@class="p2"]')

            layout_dict['layout_price'] = re.sub(r'\n.+', '', info_li.xpath('string(p[@class="p2"])').extract_first())
            layout_dict['last_update_time'] = p2.xpath('span[contains(@class,"p2-time")]/text()').extract_first()

            p3 = info_li.xpath('p[@class="p3"]')
            key = p3.xpath('text()').extract_first()
            value = p3.xpath('span/text()').extract_first()
            layout_dict[key] = value

            layout_dict['tags'] = info_li.xpath('p[@class="p4"]/span/text()').extract()
            print(layout_dict)
            print('--------------')
        return
