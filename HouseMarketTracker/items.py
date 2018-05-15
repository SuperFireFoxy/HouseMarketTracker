# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseDetail():
    def __init__(self, basic_info, opening_info, plan_info, pre_sales_info, facility_info):
        self.basic_info = basic_info
        self.opening_info = opening_info
        self.plan_info = plan_info
        self.pre_sales_info = pre_sales_info
        self.facility_info = facility_info

    @staticmethod
    def self_define_serializer(var):
        # return json.dumps(var, ensure_ascii=False, default=lambda o: o.__dict__)
        return var.__dict__


class HouseImages():
    def __init__(self, prototype_room, design_sketch, amenities, realistic_picture):
        self.prototype_room = prototype_room
        self.design_sketch = design_sketch
        self.amenities = amenities
        self.realistic_picture = realistic_picture

    @staticmethod
    def self_define_serializer(var):
        # return json.dumps(var, ensure_ascii=False, default=lambda o: o.__dict__)
        return var.__dict__


class HousemarkettrackerItem(scrapy.Item):
    home_page = scrapy.Field(serializer=str)
    house_name = scrapy.Field(serializer=str)
    house_detail = scrapy.Field(serializer=HouseDetail.self_define_serializer)
    house_images = scrapy.Field(serializer=HouseDetail.self_define_serializer)
    house_layout = scrapy.Field(serializer=HouseDetail.self_define_serializer)
    pass
