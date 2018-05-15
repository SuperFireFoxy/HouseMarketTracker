# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import gridfs
import requests
from pymongo import MongoClient
from tornado import concurrent


class HousemarkettrackerPipeline(object):
    def __init__(self):
        # 链接数据库
        uri = "mongodb://hid:fuck2012@192.168.2.119/house_info_db_2018-05-14?authMechanism=MONGODB-CR"
        self.client = MongoClient(uri)

        # self.client = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT,
        #                           authMechanism='SCRAM-SHA-1')
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings.MONGO_USER, settings.MONGO_PSW)
        # time_str = time.strftime("_%Y-%m-%d", time.localtime())
        self.db = self.client.get_database(settings.MONGO_DB)  # 获得数据库的句柄
        self.coll = self.db.get_collection(settings.MONGO_COLL)  # 获得collection的句柄
        self.fs = gridfs.GridFS(self.db, settings.MONGO_COLL + "_images")

        # self.oldloop = asyncio.get_event_loop()
        logging.getLogger("urllib3").setLevel(logging.WARNING)

    def process_item(self, item, spider):
        postItem = dict(item)
        postItem['_id'] = item['house_name'] + ':' + item['home_page']
        self.coll.insert(doc_or_docs=postItem, check_keys=False, continue_on_error=True)  # 向数据库插入一条记录

        # self.process_images(item)
        return item

    def process_images(self, item):
        urls = []
        for list in item['house_images'].values():
            for pic_url in list:
                urls.append(pic_url)
                # tasks.append(asyncio.ensure_future(self.download_and_store_image(pic_url)))
                # images = requests.get(pic_url).content
                # self.fs.put(images, _id=pic_url)
        for layout in item['house_layout']:
            layout_url = layout['layout_image_url']
            urls.append(layout_url)
            # tasks.append(asyncio.ensure_future(self.download_and_store_image(layout_url)))
            # images = requests.get(layout_url).content
            # self.fs.put(images, _id=layout_url)
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # loop = asyncio.get_event_loop()
        executor = concurrent.futures.ThreadPoolExecutor(100)
        for url in urls:
            executor.submit(self.download_and_store_image, url)
        # loop.run_until_complete(asyncio.wait(tasks))
        executor.shutdown(wait=True)

        # loop.close()

    def download_and_store_image(self, url):
        image = self.download_image(url)
        self.fs.put(image, _id=url)

    def download_image(self, url):
        return requests.get(url).content


if __name__ == "__main__":
    cd = HousemarkettrackerPipeline()
    item = {"hello": "world"}
    cd.process_item(item, None)
