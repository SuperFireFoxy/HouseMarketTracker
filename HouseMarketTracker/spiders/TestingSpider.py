import scrapy

from HouseMarketTracker.items import HousemarkettrackerItem
from HouseMarketTracker.parser.CommentParser import CommentParser
from HouseMarketTracker.parser.ParseUtil import ParseUtil


class TestingSpider(scrapy.Spider):
    name = "test_spider"
    allowed_domains = ["lianjia.com"]
    start_urls = ['https://cd.fang.lianjia.com/loupan/p_hdwjhfaazop/pinglun/']

    def start_requests(self):
        item = HousemarkettrackerItem()
        # item['house_name'] = building.xpath('@title').extract_first()
        # item['home_page'] = root_url
        meta = {}
        meta['item'] = item
        meta['root_url'] = 'https://cd.fang.lianjia.com/loupan/p_hdwjhfaazop/'
        root_url = self.start_urls[0]
        yield from ParseUtil.start_request(root_url, self.parse, meta)

    def parse(self, response):
        yield from CommentParser().parse(response)
