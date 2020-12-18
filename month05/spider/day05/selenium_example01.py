"""
打开浏览器, 输入百度的url地址
"""
from selenium import webdriver

# 1. 打开浏览器 - 创建浏览器对象
driver = webdriver.Chrome()

# 2. 输入百度url地址
driver.get(url='https://www.baidu.com/')
html = driver.page_source

print(html)

driver.quit()