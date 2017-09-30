# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class B2BspiderItem(scrapy.Item):
    search_word = scrapy.Field()
    business_place= scrapy.Field()
    business_type= scrapy.Field()
    business_name= scrapy.Field()
    business_body= scrapy.Field()
    business_person= scrapy.Field()
    business_iphone= scrapy.Field()

