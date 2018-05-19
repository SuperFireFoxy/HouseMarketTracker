import re

from HouseMarketTracker.parser.DetailParser import DetailParser
from HouseMarketTracker.parser.ParseUtil import ParseUtil


class HouseHomePageParser():

    def parse(self, response):
        # print(response.body.decode('utf-8'))

        meta = response.meta
        item = meta['item']
        item['house_layout'] = self.parse_layout(response)

        house_detail_url = meta['root_url'] + 'xiangqing/'
        print(house_detail_url + '---------------------------------')
        yield from ParseUtil.start_request(house_detail_url, DetailParser().parse, meta)

    def parse_layout(self, response):
        layout_list = []

        layout_ul_s = response.xpath('//ul[@class="clear house-det"]')
        for layout_ul in layout_ul_s:
            layout_dict = {}
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
            layout_list.append(layout_dict)
        return layout_list

    def parse_unit_info(self, response):
        return
