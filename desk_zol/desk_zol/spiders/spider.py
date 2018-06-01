# -*- coding: utf-8 -*-
from scrapy import Request
import scrapy
from desk_zol.items import DeskZolItem

class Spider(scrapy.Spider):
    name = 'Desk'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn']
    base_url = 'http://desk.zol.com.cn'
    img_urls = []
    url_link = []

    def start_requests(self):
        url = 'http://desk.zol.com.cn'
        yield Request(url, callback=self.get_urls)

    def get_urls(self, response):
        url_link = response.xpath('//div[@class="main"]//a[@class="pic"]/@href').extract()
        for i in url_link:
            url = self.base_url + i
            yield Request(url, callback=self.get_img_url)
            # 取出图集所在地址并传给函数 get_img_url

    def get_img_url(self, response):
        self.url_link = []
        self.img_urls = []
        url_link = response.xpath('//ul[@id="showImg"]//li/a/@href').extract()
        name = response.xpath('//a[@id="titleName"]/text()').extract()[0]
        for i in url_link:
            url = 'http://desk.zol.com.cn' + i
            yield Request(url, callback=self.get_img, meta={'url': url, 'name':name})
        # yield Request(url, callback=self.parse, meta={'url': url_link, 'name': name}, dont_filter=True)

    def get_img(self, response):
        url_link = []
        img_urls = []
        item = DeskZolItem()
        img_url = response.xpath('//img[@id="bigImg"]/@src').extract()[0]
        name = response.xpath('//a[@id="titleName"]/text()').extract()[0]
        # if names == response.meta['name']:
        #     self.img_urls.append(img_url)
        #     self.url_link.append((response.meta['url']))
        url_link.append(response.meta['url'])
        img_urls.append(img_url)
        item['name'] = name
        item['img_urls'] = img_urls
        item['url'] = url_link
        yield item

    # def parse(self, response):
    #     item = DeskZolItem()
    #     # 利用xpath取出所需内容
    #     # img_urls = response.xpath('//ul[@id="showImg"]//li//a//img/@src|//ul[@id="showImg"]//li//a//img/@srcs').extract()
    #     item['name'] = response.meta['name']
    #     item['img_urls'] = self.img_urls
    #     item['url'] = self.url_link
    #     yield item





