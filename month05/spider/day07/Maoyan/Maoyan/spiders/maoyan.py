# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    url = 'https://maoyan.com/board/4/?offset={}0'

    def start_requests(self):
        """生成所有要抓取的URL地址, 交给调度器入队列"""
        for o in range(11):
            page_url = self.url.format(o)
            # 交给调度器入队列
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        dd_list = response.xpath('//dl/dd')
        print(len(dd_list))
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('.//p[@class="name"]/a/@title').get()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get()

            yield item

