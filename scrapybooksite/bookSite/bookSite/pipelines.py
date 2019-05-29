# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os.path
from scrapy.exceptions import DropItem
from booksite.items import BookSiteMainItem


class BooksitePipeline(object):

    def open_spider(self, spider):
        self.file = open(r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\jsonfiles\books.jl", 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # The if instance ensures that the write data is allowed in this function.
        if isinstance(item, BookSiteMainItem):
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
