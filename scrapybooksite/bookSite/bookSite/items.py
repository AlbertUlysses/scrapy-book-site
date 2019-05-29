# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookSiteMainItem(scrapy.Item):
    # Items returned for the first page scraped.
    category_name = scrapy.Field()
    category_link = scrapy.Field()
    
    # Items returned for the second batch scraped.
    book_name = scrapy.Field()
    book_link = scrapy.Field()

    # Items returned for the third batch scraped.
    full_bookname = scrapy.Field()
    priceinpounds = scrapy.Field()
    rating = scrapy.Field()
    upc = scrapy.Field()
    producttype = scrapy.Field()
    priceexcludetax = scrapy.Field()
    priceincludetax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    numberavailable = scrapy.Field()
    numberofreviews = scrapy.Field()

