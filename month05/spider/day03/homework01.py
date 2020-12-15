import pymysql
import requests
import time
from fake_useragent import UserAgent
from lxml import etree


class ProxySpider():
	def __init__(self):
		self.url = 'https://www.kuaidaili.com/free/inha/{}/'
		self.test_url = 'http://httpbin.org/get'
		self.db_dict = {
			"host": "localhost",
			"port": 3306,
			"user": "root",
			"password": "123456",
			"database": "fgo",
			"charset": "utf8"
		}
		self.db = pymysql.connect(**self.db_dict)
		self.cur = self.db.cursor()


	def get_ip(self, url):
		headers = {'User-Agent': UserAgent().random}
		html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
		eobj = etree.HTML(html)
		tr_list = eobj.xpath('//tbody/tr')
		for tr in tr_list:
			ip = tr.xpath('./td[@data-title="IP"]/text()')[0]
			print(ip)
			port = tr.xpath('./td[@data-title="PORT"]/text()')[0]
			print(port)
			if self.test_ip(ip, port, headers):
				self.save_ip(ip, port)

	def test_ip(self, ip, port, headers):
		proxy = "{}:{}".format(ip, port)
		proxies = {
			'http': 'http://{}'.format(proxy),
			'https': 'https://{}'.format(proxy),
		}
		try:
			resp = requests.get(url=self.test_url, headers=headers, proxies=proxies, timeout=3)
			if resp.status_code == 200:
				return True
			else:
				print(proxy, '不可用')
				return False
		except Exception as e:
			print('error is', e)
			print(proxy, '同样不可用')
			return False

	def save_ip(self, ip, port):
		print('{}:{}\033[31m可用\033[0m'.format(ip, port))
		sql = 'insert into proxies (ip, port) values (%s, %s);'
		item = [ip, port]
		self.cur.execute(sql, item)
		self.db.commit()

	def crawl(self):
		for page in range(1, 101):
			page_url = self.url.format(page)
			self.get_ip(page_url)
			time.sleep(5)
		self.cur.close()
		self.db.close()

if __name__ == '__main__':
	spider = ProxySpider()
	spider.crawl()