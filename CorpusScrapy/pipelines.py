# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os

class NewsPipeline(object):
    def create_dir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def process_item(self, item, spider):
        if item['content'] and len(item['content'].strip()) > 0:
            cur_path = os.path.join('./data', item['article_class'])
            self.create_dir(cur_path)
            with open(os.path.join(cur_path, item['title']), 'wb') as f:
                f.write(item['content'].encode('utf-8'))
#            line = json.dumps(dict(item)) + '\n'
#            self.file.write(line)
        return item

    def open_spider(self, spider):
        self.create_dir('data')
#        self.file = open('item.jl', 'w')

#    def close_spider(self, spider):
#        self.file.close()
