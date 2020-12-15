"""
链家二手房抓取
"""
import pymongo
import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random

class LianjiaSpider():
    def __init__(self):
        self.url = 'https://sh.lianjia.com/ershoufang/pg{}/'
        self.conn = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.conn['housedb']
        self.house_set = self.db['houseset']

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析函数"""
        eobj = etree.HTML(html)
        div_list = eobj.xpath('//div[@class="info clear"]')
        for div in div_list:
            item = {}
            title_list = div.xpath('./div[@class="title"]//a/text()')
            item['title'] = title_list[0].strip() if title_list else None
            name_list = div.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['name'] = name_list[0].strip() if name_list else None
            add_list = div.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = add_list[0].strip() if add_list else None
            info_list = div.xpath('.//div[@class="houseInfo"]/text()')
            item['info'] = info_list[0].strip() if info_list else None
            total_price_list = div.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total_price'] = total_price_list[0].strip() if total_price_list else None
            unit_price_list = div.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit_price'] = unit_price_list[0].strip() if unit_price_list else None
            self.house_set.insert_one(item)
            print(item)

    def crawl(self):
        for page in range(1, 3):
            page_url = self.url.format(page)
            self.get_html(page_url)
            # 控制频率
            time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.crawl()