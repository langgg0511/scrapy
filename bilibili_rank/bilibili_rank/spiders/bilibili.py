# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import time
import json
from bilibili_rank.items import BilibiliRankItem, BilibiliDictItem
#爬取bilibili排行榜
#日期2018/3/23

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    base_url = 'https://www.bilibili.com/index/rank/{range_menu}-{time}-{rank_catalogy}.json'
    base_video_url = 'https://www.bilibili.com/video/av{aid}/'
    #range_menu->按全站&原创&新番&影视&新人排行
    #time->按日期排行分 1/3/7/30
    #rank_catalogy->按类别排行，对照其ID
    start_urls = ['https://www.bilibili.com/ranking']

    def start_requests(self):
        yield Request(self.start_urls[0], callback=self.get_url)

    def get_url(self, response):#获取JSON以及参数字典
        range_menu = response.xpath('//ul[@id="rank_menu"]//li//@type').extract()
        range_menu_txt = response.xpath('//ul[@id="rank_menu"]//li//span[@class="txt"]/text()').extract()
        rank_catalogy = response.xpath('//ul[@id="rank_catalogy_tab"]//li/@tid').extract()
        rank_catalogy_txt = response.xpath('//ul[@id="rank_catalogy_tab"]//li/text()').extract()
        range_time = response.xpath('//div[@class="rank-tab-select"]/div[2]/ul[@class="list"]//li/@range').extract()
        range_time_txt = response.xpath('//div[@class="rank-tab-select"]/div[2]/ul[@class="list"]//li/text()').extract()
        # print(range_time)
        # print(range_time_txt)#问题所在

        bangumi_dict = {'13': '番剧', '167': '国产动画'}
        bangumi_list = ['13', '167']
        cinema_dict = {'177': '纪录片', '23': '电影', '11': '电视剧'}
        cinema_list = ['177', '23', '11']
        menu_dic = dict(zip(range_menu, range_menu_txt))
        catalogy_dic = dict(zip(rank_catalogy, rank_catalogy_txt))
        time_dic = dict(zip(range_time, range_time_txt))
        # item_list = BilibiliDictItem()
        # print(range_menu, range_menu_txt, rank_catalogy, rank_catalogy_txt, range_time, range_time_txt)
        #循环所有排行榜
        for menu in range_menu:    # 5     rank-tab-select
            for times in range_time:
                if menu == 'bangumi':
                    for catalogy in bangumi_list:  # 12 rank_catalogy
                        pass
                        # url_json = self.base_url.format(range_menu=menu, time=times, rank_catalogy=catalogy)
                        # time.sleep(1)
                        # tables_name = menu + '_' + times + '_' + catalogy
                        # # item_list['tables_name'] = tables_name
                        # # yield item_list     #获取数据库表名称
                        # yield Request(url_json, meta={'menu': menu, 'catalogy': catalogy, 'times': times,
                        #                               'menu_value': menu_dic[menu],
                        #                               'catalogy_value': bangumi_dict[catalogy],
                        #                               'times_value': time_dic[times],
                        #                               'menu_list': range_menu, 'times_list': range_time,
                        #                               'catalogy_list': rank_catalogy,
                        #                               'table_name': tables_name},
                        #               dont_filter=True,
                        #               callback=self.get_json)
                elif menu == 'cinema':
                    for catalogy in cinema_list:  # 12 rank_catalogy
                        menus = 'all'
                        url_json = self.base_url.format(range_menu=menus, time=times, rank_catalogy=catalogy)
                        time.sleep(1)
                        tables_name = menu + '_' + times + '_' + catalogy
                        # item_list['tables_name'] = tables_name
                        # yield item_list     #获取数据库表名称
                        yield Request(url_json, meta={'menu': menu, 'catalogy': catalogy, 'times': times,
                                                      'menu_value': menu_dic[menu],
                                                      'catalogy_value': cinema_dict[catalogy],
                                                      'times_value': time_dic[times],
                                                      'menu_list': range_menu, 'times_list': range_time,
                                                      'catalogy_list': rank_catalogy,
                                                      'table_name': tables_name},
                                      dont_filter=True,
                                      callback=self.get_json)
                else:
                    for catalogy in rank_catalogy:  # 12 rank_catalogy
                        url_json = self.base_url.format(range_menu=menu, time=times, rank_catalogy=catalogy)
                        time.sleep(1)
                        tables_name = menu + '_' + times + '_' + catalogy
                        # item_list['tables_name'] = tables_name
                        # yield item_list     #获取数据库表名称
                        yield Request(url_json, meta={'menu': menu, 'catalogy': catalogy, 'times': times,
                                                      'menu_value': menu_dic[menu],
                                                      'catalogy_value': catalogy_dic[catalogy],
                                                      'times_value': time_dic[times],
                                                      'menu_list': range_menu, 'times_list': range_time,
                                                      'catalogy_list': rank_catalogy,
                                                      'table_name': tables_name},
                                      dont_filter=True,
                                      callback=self.get_json)
        #4  range_time
        # print(url_json)

    def get_json(self, response):   #获取详细信息
        jsobj = json.loads(response.body)
        lists = jsobj['rank']['list']
        item_list = BilibiliDictItem()
        item_list['tables_name'] = response.meta['table_name']
        yield item_list
        #
        # menu_list = response.meta['menu_list']
        # times_list = response.meta['times_list']
        # catalogy_list = response.meta['catalogy_list']
        # for menu_name in menu_list:
        #     for times_name in times_list:
        #         for catalogy_name in catalogy_list:
        #             tables_name = menu_name + '_' + times_name + '_' + catalogy_name
        #             item_list['tables_name'] = tables_name
        #             # print("11111111111111111111111111111111111")
        #             # print(item_list)
        #             yield item_list
        for i in range(0, len(lists)):
            item = BilibiliRankItem()
            aid = lists[i]['aid']   #视频ID
            author = lists[i]['author']     #作者名
            coins = lists[i]['coins']       #硬币数量
            duration = lists[i]['duration']     #视频长度
            mid = lists[i]['mid']       #作者ID
            play = lists[i]['play']     #播放数
            pts = lists[i]['pts']       #综合评分
            title = lists[i]['title']   #标题
            video_review = lists[i]['video_review']      #总弹幕数
            # pic = lists[i]['pic']       #封面图片
            video_url = self.base_video_url.format(aid=aid)
            tables_name2 = response.meta['menu'] + '_' + response.meta['times'] + '_' + response.meta['catalogy']
            item['aid'] = aid
            item['author'] = author
            item['coins'] = coins
            item['duration'] = duration
            item['mid'] = mid
            item['play'] = play
            item['pts'] = pts
            item['title'] = title
            item['video_review'] = video_review
            item['video_url'] = video_url
            item['times'] = response.meta['times_value']
            item['menu'] = response.meta['menu_value']
            item['catalogy'] = response.meta['catalogy_value']
            item['tables_name'] = tables_name2
            # print(item)
            yield item




