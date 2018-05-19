# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import time

import gridfs
import requests
from pymongo import MongoClient
from tornado import concurrent

from HouseMarketTracker import settings


class HousemarkettrackerPipeline(object):
    def __init__(self):
        self.client, self.db, self.coll, self.fs = self.init_db()
        logging.getLogger("urllib3").setLevel(logging.WARNING)

    def init_db(self):
        date_str = time.strftime("_%Y-%m-%d", time.localtime())
        db_name = settings.MONGO_DB + date_str
        auth_mechanism = 'SCRAM-SHA-1'
        if settings.MONGO_HW == "BBB":
            auth_mechanism = 'MONGODB-CR'
        # use admin user to drop target database
        client = MongoClient(host=settings.MONGO_HOST,
                             port=settings.MONGO_PORT,
                             username=settings.MONGO_ADMIN_USER,
                             password=settings.MONGO_ADMIN_PSW,
                             authMechanism=auth_mechanism)
        client.drop_database(db_name)

        # use admin user to create database and costumer user
        db = client.get_database(db_name)
        roles = [{'role': 'dbOwner', 'db': db_name}]
        db.add_user(name=settings.MONGO_USER, password=settings.MONGO_PSW, roles=roles)
        coll = db.get_collection(settings.MONGO_COLL)
        fs = gridfs.GridFS(db, settings.MONGO_COLL + "_images")

        # coll.insert({"hello": "world"})
        return client, db, coll, fs


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
    # cd.process_item(item, None)
    cd.init_db()
