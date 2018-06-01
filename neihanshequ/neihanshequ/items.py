# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeihanshequItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    digg = scrapy.Field()
    bury = scrapy.Field()
    repin = scrapy.Field()
    comment = scrapy.Field()
    share = scrapy.Field()
