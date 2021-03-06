from HouseMarketTracker.items import HouseDetail
from HouseMarketTracker.parser.HouseHomePageParser import HouseHomePageParser
from HouseMarketTracker.parser.ParseUtil import ParseUtil


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
        home_page_url = meta['root_url']
        yield from ParseUtil.start_request_with_lua(home_page_url, HouseHomePageParser().parse, meta)

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
        facility_li_s = response.xpath('//h2[text()="配套信息"]/following::ul[@class="x-box"]/li')
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
                        value_title = value.xpath('@title').extract()[0]
                        value_text = value.xpath('text()').extract()[0]
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
