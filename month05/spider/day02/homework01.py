"""
正则抓取豆瓣图书top250书籍信息
抓取目标：书籍名称、书籍信息、书籍评分、书籍评论人数、书籍描述
"""
import re

import requests

url = 'https://book.douban.com/top250?icn=index-book250-all'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

resp = requests.get(url=url, headers=headers).text
print(1)

regex = '''<td valign="top".*?title="(.*?)".*?p class="pl">(.*?)</p.*?span class="pl">(.*?)</span.*?span class="inq">(.*?)</span.*?'''

book_list = re.findall(regex, resp, re.S)
print(book_list)

# for book in book_list:
#     print(book)