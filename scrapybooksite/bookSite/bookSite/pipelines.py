# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os.path
import hashlib
from scrapy.exceptions import DropItem


class BooksitePipeline(object):
    
    def open_spider(self, books):
        self.file = open(r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\jsonfiles\books.json", 'w')

    def close_spider(self, books):
        self.file.close()

    def process_item(self, item, books):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item



