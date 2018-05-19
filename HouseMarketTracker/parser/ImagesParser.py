import re

from HouseMarketTracker.parser.CommentParser import CommentParser
from HouseMarketTracker.parser.ParseUtil import ParseUtil


class ImagesParser():

    def parse(self, response):
        meta = response.meta
        item = meta['item']

        all_album_divs = response.xpath('//div[@class="tab-group"]')
        image_dict = {}
        for album_div in all_album_divs:
            title = album_div.xpath('h4/a/text()').extract_first()
            title = re.search(r'(.+?)（\d*）', title).group(1)
            image_li_s = album_div.xpath('ul/li')
            image_list = []
            for image_li in image_li_s:
                image_url = image_li.xpath('a/img/@src').extract_first()
                image_url = re.sub(r'235x178', '1000x', image_url)
                image_list.append(image_url)
            image_dict[title] = image_list
        item['house_images'] = image_dict

        comments_url = meta['root_url'] + 'pinglun/'
        yield from ParseUtil.start_request(comments_url, CommentParser().parse, meta)
        # yield item
        # house_layout_url = meta['root_url'] + 'huxingtu/'
        # yield from ParseUtil.start_request(house_layout_url, HouseLayoutParser().parse, meta)
        # print(meta)
