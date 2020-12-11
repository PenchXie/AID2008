import requests
import re
import time
import random
import redis
from hashlib import md5

class NovelSpider():
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        self.m = md5()

    def get_html(self, url):
        """功能函数1: 请求"""
        html = requests.get(url=url, headers=self.headers).text
        return html

    def refunc(self, regex, html):
        """功能函数2: 正则解析函数"""
        r_list = re.findall(regex, html, re.S)
        return r_list

    def crawl(self, first_url):
        """爬虫逻辑函数"""
        first_html = self.get_html(first_url)
        first_regex = '<div class="caption">.*?href="(.*?)" title="(.*?)".*?<small ' \
                'class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p></div>'
        first_list = self.refunc(first_regex, first_html)
        for one_novel_tuple in first_list:
            item = {}
            item['title'] = one_novel_tuple[1].strip()
            item['href'] = one_novel_tuple[0].strip()
            item['author'] = one_novel_tuple[2].strip()
            item['comment'] = one_novel_tuple[3].strip()
            # 获取此小说中剩余数据
            self.parse_second_page(item)


    def parse_second_page(self, item):
        """二级页面解析函数"""
        second_html = self.get_html(url=item['href'])
        second_regex = '<dd class="col-md-4"><a href="(.*?)">(.*?)</a></dd>'
        second_list = self.refunc(second_regex, second_html)
        for second_novel_tuple in second_list:
            item['son_title'] = second_novel_tuple[1]
            item['son_href'] = second_novel_tuple[0]
            print(item)
            finger = self.md5_href(item['son_href'])
            if self.r.sadd('novel:spiders', finger) == 1:
                print('开始抓取此章节', item['son_title'])
            else:
                print('此章节已抓取过')

    def run(self):
        for page in range(1, 2):
            page_url = self.url.format(page)
            self.crawl(page_url)
            time.sleep(random.randint(1, 3))

    def md5_href(self, href):
        self.m.update(href.encode())
        return self.m.hexdigest()


if __name__ == '__main__':
    spider = NovelSpider()
    spider.run()