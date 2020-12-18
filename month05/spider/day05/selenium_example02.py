from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url='https://www.baidu.com/')

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('One Piece')

driver.find_element_by_xpath('//*[@id="su"]').click()