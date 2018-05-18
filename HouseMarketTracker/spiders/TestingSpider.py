import scrapy
from scrapy_splash import SplashRequest

from HouseMarketTracker.parser.CommentParser import CommentParser


class TestingSpider(scrapy.Spider):
    name = "test_spider"
    allowed_domains = ["lianjia.com"]
    start_urls = ['https://cd.fang.lianjia.com/loupan/p_xxwjyntabaip/pinglun/']

    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse,
                            args={
                                # optional; parameters passed to Splash HTTP API
                                'wait': 3,

                                # 'url' is prefilled from request url
                                # 'http_method' is set to 'POST' for POST requests
                                # 'body' is set to request body for POST requests
                            })

    def parse(self, response):
        yield from CommentParser().parse(response)
