from math import ceil

from HouseMarketTracker.parser.ParseUtil import ParseUtil


class NewsParser:
    def parse(self, res):
        news_list = []
        news_div_s = res.xpath('//div[@class="dongtai-one for-dtpic"]')
        for new_div in news_div_s:
            news_dict = {}
            news_dict['tag'] = new_div.xpath('a/span[@class="a-tag"]/text()').extract_first()
            news_dict['title'] = new_div.xpath('a/span[@class="a-title"]/text()').extract_first()
            news_dict['time'] = new_div.xpath('a/span[@class="a-time"]/text()').extract_first()
            news_dict['content'] = new_div.xpath('child::*//div[@class="a-word"]/a/text()').extract_first()
            news_dict['link'] = new_div.xpath('child::*//div[@class="a-word"]/a/@href').extract_first()

            news_list.append(news_dict)

        meta = res.meta
        item = meta['item']

        if item.get('house_news') is None:
            item['house_news'] = news_list
        else:
            item['house_news'] += news_list

        page = res.xpath('//div[@class="page-box"]')
        current_page_str = page.xpath('@data-current').extract_first()
        if current_page_str is None:
            yield item
        else:
            current_page_index = int(current_page_str)
            total_count = int(page.xpath('@data-total-count').extract_first())
            total_pages = ceil(total_count / 20.0)
            if current_page_index < total_pages:
                next_page_url = meta['root_url'] + 'dongtai/pg' + str(current_page_index + 1)
                yield from ParseUtil.start_request(next_page_url, NewsParser().parse, meta)
            else:
                yield item
