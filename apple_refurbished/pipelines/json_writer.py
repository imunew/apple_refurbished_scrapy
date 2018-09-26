# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os


class JsonWriterPipeline(object):

    OUTPUT_DIR = '.output'
    items = []

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        if not os.path.exists(self.OUTPUT_DIR):
            os.mkdir(self.OUTPUT_DIR)

        with codecs.open(os.path.join(self.OUTPUT_DIR, 'items.json'), 'w', 'utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=2)

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item
