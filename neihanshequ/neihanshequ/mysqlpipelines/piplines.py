# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .sql import Sql
from neihanshequ.items import NeihanshequItem

class NeihanshequPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, NeihanshequItem):
            nh_id = item['id']
            ret = Sql.select_id(nh_id)
            if ret[0] == 1:
                print('存在')
                pass
            else:
                name = item['name']
                nh_text = item['title']
                digg = item['digg']
                repin = item['repin']
                nh_comment = item['comment']
                nh_share = item['share']
                bury = item['bury']
                Sql.insert_dd_name(name, nh_text, digg, bury, nh_comment, nh_share, repin, nh_id)
                print('开始存储')