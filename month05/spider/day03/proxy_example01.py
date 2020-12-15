"""代理IP"""
import requests
from fake_useragent import UserAgent
url = 'http://httpbin.org/get'
headers = {'User-Agent': UserAgent().random}

proxies = {
    'http': 'http://124.238.238.50:80',
    'https': 'https://124.238.238.50:80',
}

html = requests.get(url=url, headers=headers, proxies=proxies).text

print(html)
