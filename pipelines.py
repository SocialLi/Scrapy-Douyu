# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from Douyu.settings import IMAGES_STORE


# ImagesPipeline 处理图片的管道类
class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imagelink = item['image_link']
        yield scrapy.Request(imagelink)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        os.rename(IMAGES_STORE + '/' + image_path[0], IMAGES_STORE + '/' +item['nickname'] + '.jpg')
        return item
