from selenium import webdriver
# 鼠标事件类
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get(url='https://www.baidu.com/')
search_node = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(search_node).perform()
driver.find_element_by_link_text('高级搜索').click()
