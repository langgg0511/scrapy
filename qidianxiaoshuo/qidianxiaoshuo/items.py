# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class QidianxiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()       #小说名
    novel_url = scrapy.Field()  #小说地址
    author = scrapy.Field()     #小说作者
    category = scrapy.Field()   #小说类别
    tag = scrapy.Field()        #小说标签
    statue = scrapy.Field()     #小说状态
    number = scrapy.Field()   #小说字数
    info = scrapy.Field()       #小说简介
    name_id = scrapy.Field()    #小说ID