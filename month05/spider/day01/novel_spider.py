"""
1. 小说链接
2. 小说名称
3. 小说作者
4. 小说简介
"""
import pymysql
import requests
import re
import time
import random


class NovelSpider():
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        self.db = pymysql.connect('localhost', 'root', '123456', 'noveldb', charset='utf8')
        self.cur = self.db.cursor()

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        # 调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """正则解析函数"""
        regex = '<div class="caption">.*?href="(.*?)" title="(.*?)".*?<small ' \
                'class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p></div>'
        novel_list = re.findall(regex, html, re.S)
        # 调用数据处理
        self.save_html(novel_list)

    def save_html(self, novel_list):
        """数据处理"""
        for novel_tuple in novel_list:
            print(novel_tuple)
            temp_list = [item for item in novel_tuple]
            ins = 'insert into novel_tab  (href, title, author, comment) values(%s,%s,%s,%s);'
            self.cur.execute(ins, temp_list)
            self.db.commit()

    def crawl(self):

        for page in range(1, 2):
            page_url = self.url.format(page)
            self.get_html(url=page_url)
            # 控制数据抓取的频率
            time.sleep(random.randint(1, 3))

        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    spider = NovelSpider()
    spider.crawl()