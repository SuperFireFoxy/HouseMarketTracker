import re
from math import ceil

from HouseMarketTracker.parser.NewsParser import NewsParser
from HouseMarketTracker.parser.ParseUtil import ParseUtil


class CommentParser:
    def parse(self, response):

        comment_dict = {}
        # header
        user_comment_key = response.xpath('//div[@class="comments-list-wrap"]/h2/text()').extract_first()
        total_score_dict = {}
        total_score_dict['综合评分'] = response.xpath('//span[@class="score"]/text()').extract_first()
        total_score_dict['评分比例'] = response.xpath('//span[@class="ratio"]/text()').extract_first()
        for score_item in response.xpath('//div[@class="item"]'):
            key = self.remove_tail(score_item.xpath('span/text()').extract_first())
            value = score_item.xpath('i/text()').extract_first()
            total_score_dict[key] = value
        comment_dict[user_comment_key] = total_score_dict
        comment_dict['comments'] = []

        meta = response.meta

        # meta['item'] = HousemarkettrackerItem()
        # meta['root_url'] = "https://cd.fang.lianjia.com/loupan/p_xxwjyntabaip/"

        item = meta['item']
        item['house_comment'] = comment_dict

        # content
        yield from self.parse_comments(response)

    def parse_comments(self, res):
        li_s = res.xpath('//li[@data-role="commentitem"]')
        comments_in_page = []
        for li in li_s:
            comment_content_dict = {}
            # user
            user = li.xpath('div[@class="l_userpic"]')
            comment_content_dict['user_image'] = user.xpath('//img/@src').extract_first()
            user_line = user.xpath('div[@class="info"]/text()').extract()
            comment_content_dict['user_name'] = self.normalize_space(user_line[0])
            comment_content_dict['user_life'] = self.normalize_space(user_line[1])
            # comment
            comment = li.xpath('div[@class="r_comment"]')
            comment_content_dict['tag'] = comment.xpath('span[@class="tag"]/text()').extract_first()
            star = comment.xpath('child::*//div[@class="star_info"]/@style').extract_first()
            star = 5 * int(re.match('.+?(\d+)%', star).group(1)) / 100
            comment_content_dict['star'] = star
            all_item_score_s = comment.xpath('child::*/div[@class="num"]/span/text()').extract()
            for specific_score in all_item_score_s:
                key_value = specific_score.split('：')
                comment_content_dict[key_value[0]] = key_value[1]
            comment_content_dict['words'] = li.xpath('child::*//div[@class="words"]/text()').extract_first()
            comment_content_dict['time'] = li.xpath('child::*//div[@class="time"]/text()').extract_first()
            comment_content_dict['like'] = li.xpath('child::*//div[@class="like"]/span/text()').extract_first()

            comments_in_page.append(comment_content_dict)

        # meta
        meta = res.meta
        item = meta['item']
        item['house_comment']['comments'] += (comments_in_page)

        current_page_str = res.xpath('//div[@class="page-box"]/@data-current').extract_first()
        if current_page_str is None:
            yield from self.start_parse_news(meta)
        else:
            current_page = int(current_page_str)
            total_pages = ceil(int(res.xpath('//div[@class="page-box"]/@data-total-count').extract_first()) / 20.0)
            next_page_rul = meta['root_url'] + 'pinglun/pg' + str(current_page + 1)

            if current_page < total_pages:

                yield from ParseUtil.start_request(next_page_rul, CommentParser().parse_comments, meta)
            else:

                yield from self.start_parse_news(meta)

    def start_parse_news(self, meta):
        news_url = meta['root_url'] + 'dongtai/'
        yield from ParseUtil.start_request(news_url, NewsParser().parse, meta)

    def remove_tail(self, str):
        return re.sub('：', '', str)

    def normalize_space(self, str):
        return re.sub('\s', '', str)
