import scrapy

from HouseMarketTracker.items import HousemarkettrackerItem
from HouseMarketTracker.parser.DetailParser import DetailParser
from HouseMarketTracker.parser.ParseUtil import ParseUtil


def get_urls():
    links = []
    for index in range(1, 119):
        links.append("https://cd.fang.lianjia.com/loupan/pg" + str(index))
    return links


class LianjiaSpider(scrapy.Spider):
    name = "house_spider"
    allowed_domains = ["lianjia.com"]
    start_urls = get_urls()


    def parse(self, response):
        buildings = response.xpath('/html/body/div[4]/ul[2]/li/a')

        for building in buildings:
            root_url = "https://cd.fang.lianjia.com" + building.xpath('@href').extract_first()

            item = HousemarkettrackerItem()
            item['house_name'] = building.xpath('@title').extract_first()
            item['home_page'] = root_url

            meta = {}
            meta['item'] = item
            meta['root_url'] = root_url

            detail_url = root_url + 'xiangqing/'
            print('start: ------' + root_url)
            yield from ParseUtil.start_request(detail_url, DetailParser().parse, meta)
