"""
向测试网站发请求确认请求头中的User-Agent
"""
import requests

url = 'http://httpbin.org/get'
html = requests.get(url=url,
                    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}).text
print(html)