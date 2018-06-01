# -*- coding: utf-8 -*-
import scrapy
from qidianxiaoshuo.items import QidianxiaoshuoItem
from scrapy.http import Request

class MySpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['https://www.qidian.com']
    base_url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page='
    start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']

    def start_requests(self):
        for i in range(1, 2):
            url = self.base_url + str(i)
            yield Request(url, callback=self.parse)

    def parse(self, response):
        url_link = response.xpath('//div[@class="book-mid-info"]/h4/a/@href').extract()
        for novel_urls in url_link:
            novel_url ='https:' + str(novel_urls)
            # print(novel_url)
            # print(novel_urls)
            yield Request(novel_url, callback=self.get_charterurl, dont_filter=True, meta={'novel_url': novel_url})
        # print('*' * 30)

    def get_charterurl(self, response):
        item = QidianxiaoshuoItem()
        name = response.xpath('//div[@class="book-info "]/h1/em/text()').extract()[0]
        author = response.xpath('//div[@class="book-info "]/h1/span/a/text()').extract()[0]
        novel_url = response.meta['novel_url']
        name_id = novel_url[-10:].strip('info/')
        tag_link = response.xpath('//div[@class="book-info "]/p[@class="tag"]/a/text()').extract()
        category = tag_link[0]
        tag = ",".join(tag_link[1:])
        statue = response.xpath('//div[@class="book-info "]/p[@class="tag"]/span/text()').extract()[0]
        number = response.xpath('//div[@class="book-info "]//p/em/text()').extract()[0]
        info = response.xpath('//div[@class="book-info "]/p[@class="intro"]/text()').extract()[0]

        item['name'] = name
        item['author'] = author
        item['novel_url'] = novel_url
        item['category'] = category
        item['tag'] = tag
        item['statue'] = statue
        item['number'] = number + '万'
        item['info'] = info
        item['name_id'] = name_id
        # print(item)
        # print('-'*30)
        yield item