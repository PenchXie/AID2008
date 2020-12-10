import requests
from urllib import parse

# 1 拼接URL
key_word = input("Input key word:")
params = parse.quote(key_word)
# print(params)
url = 'http://www.baidu.com/s?wd={}'.format(params)
# print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1'
                         ' (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

# 2 发请求获取响应
html = requests.get(url=url, headers=headers).text
# print(html)

# 3 保存文件
filename = '{}.html'.format(key_word)
with open(filename, 'w') as f:
    f.write(html)