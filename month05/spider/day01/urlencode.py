"""
终端输入关键字.将百度的响应内容保存到本地文件
"""
import requests
from urllib import parse

key_word = input("Input key word:")
params = parse.urlencode({'wd': key_word})
# print(params)
url = 'http://www.baidu.com/s?{}'.format(params)
# print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1'
                         ' (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
html = requests.get(url=url, headers=headers).text
# print(html)
filename = '{}.html'.format(key_word)
with open(filename, 'w') as f:
    f.write(html)