# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名, 用来运行爬虫: scrapy crawl 爬虫名
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        """解析提取数据"""
        # response.xpath() : [<>, <>, ...]
        # extract(): ['百度一下,你就知道']
        # extract_first(): '百度一下,你就知道', 相当于get()
        # get(): '百度一下,你就知道', 等同于extract_first()
        r = response.xpath('//title/text()').get()
        print(r)
        # text属性:响应内容-字符串
        print(response.text)
        # body属性:响应内容-字节串
        print(response.body)
