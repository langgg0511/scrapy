# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DeskZolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()       #图片名称
    img_urls = scrapy.Field()    #图片img
    url = scrapy.Field()        #图片所在地址
    pass

