import random
import time

import requests
from fake_useragent import UserAgent
from lxml import etree


class DoubanBookSpider():
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        # utf-8: 右键查看网页源代码-charset
        # ignore: 解码遇到不识别的字符直接忽略
        html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
        self.parse_html(html)

    def parse_html(self, html):
        """xpath解析提取数据"""
        eobj = etree.HTML(html)
        table_list = eobj.xpath('//table')
        for table in table_list:
            item = {}
            title_list = table.xpath('.//div[@class="pl2"]/a/@title')
            item['title'] = title_list[0].strip() if title_list else None
            info_list = table.xpath('.//p[1]/text()')
            item['info'] = info_list[0].strip() if info_list else None
            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            item['score'] = score_list[0].strip() if score_list else None
            nums_list = table.xpath('.//span[@class="pl"]/text()')
            item['nums'] = nums_list[0][1:-1].strip()[:-3] if nums_list else None
            comment_list = table.xpath('.//span[@class="inq"]/text()')
            item['comment'] = comment_list[0].strip() if comment_list else None
            print(item)

    def crawl(self):
        for page in range(2):
            page_url = self.url.format(page * 25)
            self.get_html(page_url)
            # 控制频率
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider = DoubanBookSpider()
    spider.crawl()