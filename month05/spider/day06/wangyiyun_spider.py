from selenium import webdriver

url = 'https://music.163.com/#/discover/toplist'
driver = webdriver.Chrome()
driver.get(url)
# 切换frame
driver.switch_to.frame('g_iframe')
tr_list = driver.find_elements_by_xpath('//table/tbody/tr')
for tr in tr_list:
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text
    item['name'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').replace('\xa0', ' ')
    item['time'] = tr.find_element_by_xpath('.//span[@class="u-dur "]').text
    item['singer'] = tr.find_element_by_xpath('.//div[@class="text"]').get_attribute('title')
    print(item)

driver.quit()