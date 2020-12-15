import requests
from lxml import etree

url = 'https://book.douban.com/top250?start=0'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
html = requests.get(url=url, headers=headers).text

parse_html = etree.HTML(html)

table_list = parse_html.xpath('//table')
print(table_list)

for table in table_list:
    title = table.xpath('.//div[@class="pl2"]/a/@title')
    print(title)
