# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookSiteMainItem(scrapy.Item):
    category_name = scrapy.Field()
    category_link = scrapy.Field()
    book_name = scrapy.Field()
    book_link = scrapy.Field()


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

