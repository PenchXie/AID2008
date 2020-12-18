"""
切换句柄
1. li = driver.window_handles
2. driver.switch_to.window(li[1])
"""
import sys
import time

import redis
from hashlib import md5
from selenium import webdriver


class MzbSpider():
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        # 设置无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url=self.url)
        # 连接redis
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def md5_href(self, href):
        """功能函数"""
        m = md5()
        m.update(href.encode())

        return m.hexdigest()

    def parse_html(self):
        """爬虫逻辑函数"""
        latest_node = self.driver.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul'
                                          '/table/tbody/tr[1]/td[2]/a')
        latest_href = latest_node.get_attribute('href')
        finger = self.md5_href(latest_href)
        if self.r.sadd('mzb:spiders', finger) == 1:
            latest_node.click()
            time.sleep(1)
            li = self.driver.window_handles
            self.driver.switch_to.window(li[1])
            tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
            for tr in tr_list:
                item = {}
                # selenium中xpath语句中不能在最后加/text()或/@属性值
                item['name'] = tr.find_element_by_xpath('./td[3]').text.strip()
                item['code'] = tr.find_element_by_xpath('./td[2]').text.strip()
                print(item)
        else:
            self.driver.quit()
            sys.exit('完成')

    def crawl(self):
        self.parse_html()


if __name__ == '__main__':
    spider = MzbSpider()
    spider.crawl()
