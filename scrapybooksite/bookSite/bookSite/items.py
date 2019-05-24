# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookSiteMainItem(scrapy.Item):
    category = scrapy.Field()
    link = scrapy.Field()


class BookCategoryItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()


class BookDataItem(scrapy.Item):
    bookname = scrapy.Field()
    priceinpounds = scrapy.Field()
    rating = scrapy.Field()
    upc = scrapy.Field()
    producttype = scrapy.Field()
    priceexcludetax = scrapy.Field()
    priceincludetac = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    numberavailable = scrapy.Field()
    numberofreviews = scrapy.Field()

#path = r"C:\Users\alber\Desktop\myWork\projects\scrapy-book-site\scrapybooksite\booksite\booksite\spiders\htmlfiles\"