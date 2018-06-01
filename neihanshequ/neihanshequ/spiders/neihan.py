# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from neihanshequ.items import NeihanshequItem
import json
import re

class NeihanSpider(scrapy.Spider):
    name = 'neihan'
    allowed_domains = ['www.neihanshequ.com']
    start_urls = ['http://www.neihanshequ.com/']
    def start_requests(self):

        for i in range(1, 101):
            time = 1500000000 + (i * 1000)
            url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}'.format(time)
            yield Request(url, callback=self.parse)

    def parse(self, response):
        item = NeihanshequItem()
        # name = response.xpath('//span[@class="name"]/text()').extract()
        # time = response.xpath('//span[@class="time timeago"]/text()').extract()
        # title = response.xpath('//div[@class="upload-txt  no-mb"]//p/text()').extract()
        # digg = response.xpath('//span[@class="digg"]/text()').extract()
        # bury = response.xpath('//span[@class="bury"]/text()').extract()
        # repin = response.xpath('//span[@class="repin"]/text()').extract()
        # comment = response.xpath('//span[@class="comment J-comment-count"]/text()').extract()
        # share = response.xpath('//span[@class="share"]/text()').extract()
        # for i in range(len(name)):
        #     item['name'] = name[i]
        #     item['time'] = time[i].strip()
        #     item['title'] = title[i]
        #     item['digg'] = digg[i]
        #     item['repin'] = repin[i]
        #     item['comment'] = comment[i]
        #     item['share'] = share[i]
        #     item['bury'] = bury[i]
        #     print(item)
        #-----------------------------------------------------------
        text = response.text
        text.encode('utf-8')
        jsons = json.loads(text)
        for i in range(0, 20):
            digg = jsons['data']['data'][i]['group']['digg_count']
            if digg > 1000:
                id = jsons['data']['data'][i]['group']['id']
                title = jsons['data']['data'][i]['group']['text']
                name = jsons['data']['data'][i]['group']['user']['name']
                bury = jsons['data']['data'][i]['group']['bury_count']
                repin = jsons['data']['data'][i]['group']['repin_count']
                comment = jsons['data']['data'][i]['group']['comment_count']
                share = jsons['data']['data'][i]['group']['share_count']
                item['name'] = name
                item['id'] = id
                item['title'] = title
                item['digg'] = digg
                item['repin'] = repin
                item['comment'] = comment
                item['share'] = share
                item['bury'] = bury
                yield item


