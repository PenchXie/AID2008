"""
driver.execute_script
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://search.jd.com/Search?keyword=%E5%80%9A%E5%A4%A9%E5%89%91&enc=utf-8'
               '&wq=%E5%80%9A%E5%A4%A9%E5%89%91&pvid=1ce40bdb1f0e452f9a4b6af460f9c7de')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

time.sleep(3)
# 提取数据
li_list = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
print(len(li_list))
driver.quit()