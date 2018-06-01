# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliRankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    aid = scrapy.Field()
    author = scrapy.Field()
    coins = scrapy.Field()
    duration = scrapy.Field()
    mid = scrapy.Field()
    play = scrapy.Field()
    pts = scrapy.Field()
    title = scrapy.Field()
    video_review = scrapy.Field()
    video_url = scrapy.Field()
    menu = scrapy.Field()
    catalogy = scrapy.Field()
    times = scrapy.Field()
    tables_name = scrapy.Field()

class BilibiliDictItem(scrapy.Item):
    # menu_list = scrapy.Field()
    # times_list = scrapy.Field()
    # catalogy_list = scrapy.Field()
    tables_name = scrapy.Field()