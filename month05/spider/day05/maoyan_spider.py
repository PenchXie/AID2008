import random
import time

from selenium import webdriver

url = 'https://maoyan.com/board/4'
# 设置无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
def parse_one_page():
    dd_list = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for dd in dd_list:
        text_list = dd.text.split('\n')
        item = {}
        item['title'] = text_list[0]
        item['actors'] = text_list[1]
        item['time'] = text_list[2]
        item['score'] = text_list[3]

while True:
    parse_one_page()
    time.sleep(random.randint(1, 3))
    try:
        driver.find_element_by_link_text('下一页').click()
    except Exception as e:
        print('抓取完成')
        break
driver.quit()