"""
第一步实现: 抓取剧情类别下的所有电影,电影总数自动获取
第二部实现效果: 根据用户输入电影类别抓取电影
"""
import re

import requests
import json
import time
import random
from fake_useragent import UserAgent


class DouBanSpider():
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'

    def get_html(self, url):
        """功能函数"""
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text

        return html

    def parse_html(self, url):
        """爬虫逻辑函数"""
        html = self.get_html(url)
        # html: [{}, {}, ...]
        html = json.loads(html)
        for one_film_dict in html:
            item = {}
            item['rank'] = one_film_dict['rank']
            item['title'] = one_film_dict['title']
            item['score'] = one_film_dict['score']
            item['time'] = one_film_dict['release_date']
            item['type'] = one_film_dict['types']
            print(item)

    def get_total(self, type_num):
        """获取某个类别下的电影总数"""
        total_url = 'https://movie.douban.com/j/chart/top_list_count?type={}' \
                    '&interval_id=100%3A90'.format(type_num)
        total_html = self.get_html(total_url)
        total_json = json.loads(total_html)
        total = total_json['total']

        return total

    def get_all_type_dict(self):
        """返回所有类别的大字典"""
        index_url = 'https://movie.douban.com/chart'
        index_html = self.get_html(index_url)
        regex = '<span><a href=".*?type_name=(.*?)&type=(\d+)&interval_id=100:90&action=">'
        # r_list: [('剧情', '11'), ...]
        r_list = re.findall(regex, index_html, re.S)

        return {item[0]: item[1] for item in r_list}

    def crawl(self):
        all_type_dict = self.get_all_type_dict()
        while True:
            try:
                [print(key, end=' ') for key in all_type_dict]
                print()
                user_c = input("请输入类别:")
                type_num = all_type_dict[user_c]
                break
            except Exception as e:
                print("该类别不存在!")
        total = self.get_total(type_num)
        for start in range(0, total, 20):
            page_url = self.url.format(type_num, start)
            self.parse_html(url=page_url)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = DouBanSpider()
    spider.crawl()
