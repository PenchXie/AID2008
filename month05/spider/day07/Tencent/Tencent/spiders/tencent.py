import scrapy
import requests
import json
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
	name = 'tencent'
	allowed_domains = ['careers.tencent.com']
	# start_urls = ['http://careers.tencent.com/search.html?keyword={}']

	def get_page(self, keyword):
		"""功能函数，获取页数"""
		url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword={}&pageIndex=1&pageSize=10&language=zh-cn&area=cn'.format(keyword)
		json_str = requests.get(url=url).text
		json_obj = json.loads(json_str)
		count = json_obj['Data']['Count']
		if count % 10:
			return count % 10 + 1
		else:
			return count % 10

	def start_requests(self):
		# keyword = input("请输入关键字:")
		keyword = "AI"
		# page = self.get_page(keyword)
		# 可增加page抓取所有页的职位信息
		url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword={}&pageIndex=1&pageSize=10&language=zh-cn&area=cn'.format(keyword)

		yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		"""解析一级页面"""
		json_obj = json.loads(response.text)
		for job in json_obj['Data']['Posts']:
			second_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={}&language=zh-cn'.format(job['PostId'])
			yield scrapy.Request(url=second_url, callback=self.detail_parse)

	def detail_parse(self, response):
		"""解析二级页面"""
		second_json_obj = json.loads(response.text)
		item = TencentItem()
		item['title'] = second_json_obj['Data']['RecruitPostName']
		item['location'] = second_json_obj['Data']['LocationName']
		item['category'] = second_json_obj['Data']['CategoryName']
		item['issued_time'] = second_json_obj['Data']['LastUpdateTime']
		item['responsibility'] = second_json_obj['Data']['Responsibility']
		item['requirement'] = second_json_obj['Data']['Requirement']

		yield item