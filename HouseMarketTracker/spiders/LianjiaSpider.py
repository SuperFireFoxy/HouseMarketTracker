import re

import scrapy
from scrapy_splash import SplashRequest

from HouseMarketTracker.items import HousemarkettrackerItem, HouseDetail


def get_urls():
    links = []
    for index in range(1, 119):
        links.append("https://cd.fang.lianjia.com/loupan/pg" + str(index))
    return links


class LianjiaSpider(scrapy.Spider):
    name = "house_spider"
    allowed_domains = ["lianjia.com"]
    start_urls = get_urls()

    # start_urls = ["https://cd.fang.lianjia.com/loupan/pg1"]

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
            yield from ParseUtil.start_request(root_url, HouseHomePageParser().parse, meta)


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

        yield item
        # house_layout_url = meta['root_url'] + 'huxingtu/'
        # yield from ParseUtil.start_request(house_layout_url, HouseLayoutParser().parse, meta)
        # print(meta)


class DetailParser():

    def parse(self, response):
        meta = response.meta
        item = meta['item']

        basic_dict = self.parse_basic_info(response)
        plan_dict = self.parse_planning_info(response)
        facility_dict = self.parse_ancillary_facility(response)
        pre_sales_list = self.parse_pre_sales(response)
        opening_info_list = self.parse_sales_info(response)

        meta = response.meta
        item['house_detail'] = HouseDetail(basic_dict, opening_info_list, plan_dict, pre_sales_list,
                                           facility_dict).__dict__
        meta['item'] = item
        image_page_url = meta['root_url'] + 'xiangce/'
        yield from ParseUtil.start_request(image_page_url, ImagesParser().parse, meta)

    def parse_basic_info(self, response):
        basic_dict = {}
        basic_info_ul = response.xpath('/html/body/div[4]/div[1]/ul[1]/li')
        for li in basic_info_ul:
            label = li.xpath('normalize-space(span[@class="label"]/text())').extract()[0]
            label_val = li.xpath('normalize-space(span[contains(@class,"label-val")]/text())').extract()[0]
            # price
            if label_val is '':
                label_val = li.xpath('normalize-space(span/span/text())').extract()[0]
            # zone
            zone = li.xpath('normalize-space(span/a/text())').extract()[0]
            if zone is not '':
                label_val += zone
            basic_dict[label] = label_val
        return basic_dict

    def parse_sales_info(self, response):
        headers = response.xpath('//li[contains(@class,"fq-thtr fq-nbd")]/span/text()').extract()
        open_times = response.xpath('//span[@class="fq-td fq-open"]/span/text()').extract()
        sale_buildings = response.xpath('//span[@class="fq-td fq-build"]/span/text()').extract()
        hand_over_times = response.xpath('//span[@class="fq-td fq-handover"]/span/text()').extract()
        phase_nums = response.xpath('//span[@class="fq-fqname"]/text()').extract()
        building_nums = response.xpath('//span[@class="fq-fqbuild"]/span/text()').extract()
        opening_info_list = []
        for ot, sa, ha, ph, bu in zip(open_times, sale_buildings, hand_over_times, phase_nums,
                                      building_nums):
            opening_info_dict = {}
            opening_info_dict[headers[0]] = ot
            opening_info_dict[headers[1]] = sa
            opening_info_dict[headers[2]] = ha
            opening_info_dict[headers[3]] = ph + bu
            opening_info_list.append(opening_info_dict)
        return opening_info_list

    def parse_planning_info(self, response):
        plan_dict = {}
        plan_li_s = response.xpath('/html/body/div[4]/div[1]/ul[3]/li')
        for li in plan_li_s:
            label = li.xpath('normalize-space(span[@class="label"]/text())').extract()[0]
            label_val = li.xpath('normalize-space(span[contains(@class,"label-val")]/text())').extract()[0]
            # house structure type
            if label_val is '':
                structure_dict = {}
                a_s = li.xpath('span/a')
                for a in a_s:
                    structure_type_label = a.xpath('normalize-space(text())').extract()[0]
                    link = a.xpath('normalize-space(@href)').extract()[0]
                    structure_dict[structure_type_label] = link
                plan_dict[label] = structure_dict
            else:
                plan_dict[label] = label_val
        return plan_dict

    def parse_ancillary_facility(self, response):
        facility_dict = {}
        facility_li_s = response.xpath('/html/body/div[4]/div[1]/ul[4]/li')
        for li in facility_li_s:
            label = li.xpath('normalize-space(span[@class="label"]/text())').extract()[0]
            label_val = li.xpath('normalize-space(span[contains(@class,"label-val")]/text())').extract()[0]
            if label_val is '':
                around_info_dict = {}
                div_s = li.xpath('div/div')
                for div in div_s:
                    around_info_label = div.xpath('normalize-space(text())').extract()[0]
                    value_list = div.xpath('span/span')
                    value_dict = {}
                    for value in value_list:
                        value_title = value.xpath('normalize-space(@title)').extract()[0]
                        value_text = value.xpath('normalize-space(text())').extract()[0]
                        value_dict[value_text] = value_title
                    around_info_dict[around_info_label] = value_dict
                facility_dict[label] = around_info_dict
            else:
                facility_dict[label] = label_val
        return facility_dict

    def parse_pre_sales(self, response):
        pre_sales_list = []
        tr_s = response.xpath('//tr')
        th_list = []
        for th_text in tr_s[0].xpath('*/text()').extract():
            th_list.append(th_text)

        for tr in tr_s[1:]:
            single_pre_sales_dict = {}
            for (value, th) in zip(tr.xpath('*/text()').extract(), th_list):
                single_pre_sales_dict[th] = value
            pre_sales_list.append(single_pre_sales_dict)
        return pre_sales_list


class HouseHomePageParser():

    def parse(self, response):
        meta = response.meta
        item = meta['item']
        item['house_layout'] = self.parse_layout(response)

        house_detail_url = meta['root_url'] + 'xiangqing/'
        print(house_detail_url + '---------------------------------')
        yield from ParseUtil.start_request(house_detail_url, DetailParser().parse, meta)

    def parse_layout(self, response):
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
            layout_list.append(layout_dict)
        return layout_list

    def parse_unit_info(self, response):
        return
# class HouseInfoParser():
#     detail_parser = DetailParser()
#     images_parser = ImagesParser()
#
#     @staticmethod
#     def parse(response):
#         item = HousepriceItem()
#         item['house_detail'] = HouseInfoParser.detail_parser.parse(response)
#         item['house_images'] = HouseInfoParser.images_parser.parse(response)


class ParseUtil():

    @staticmethod
    def start_request(url, parse_func, meta):
        yield SplashRequest(url=url, callback=parse_func, meta=meta,
                            args={
                                # optional; parameters passed to Splash HTTP API
                                'wait': 5,

                                # 'url' is prefilled from request url
                                # 'http_method' is set to 'POST' for POST requests
                                # 'body' is set to request body for POST requests
                            })
