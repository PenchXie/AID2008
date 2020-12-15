"""
1.先从帖子中提取视频链接
2.向视频链接发请求,将视频保存到本地
"""
import os

import requests
from lxml import etree
from fake_useragent import UserAgent

url = 'https://tieba.baidu.com/p/7146936032'
headers = {'User-Agent': UserAgent().random}
html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
# print(html)

eobj = etree.HTML(html)
src = eobj.xpath('//div[@class="video_src_wrapper"]/embed/@data-video')[0]
print(src)

# 创建保存目录结构
directory = '/home/tarena/video'
if not os.path.exists(directory):
    os.makedirs(directory)

video_html = requests.get(url=src, headers=headers).content
filename = '{}{}.mp4'.format(directory, src[:-20])
with open(filename, 'wb') as f:
    f.write(video_html)
