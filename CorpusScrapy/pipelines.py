# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class NewsPipeline(object):
    def process_item(self, item, spider):
        if item['content'] and len(item['content'].strip()) > 0:
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file = open('item.jl', 'w')

    def close_spider(self, spider):
        self.file.close()
