from selenium import webdriver

url = 'https://mail.163.com/'
driver = webdriver.Chrome()
driver.get(url)
# 不能抓包复制节点, 节点后id随机生成,只在当前页面有效
iframe_node = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(iframe_node)
driver.find_element_by_name('email').send_keys('demag')
# driver.find_element_by_xpath('//*[@id="auto-id-1608176486932"]').send_keys('demag')
driver.find_element_by_name('password').send_keys('123456')
# driver.find_element_by_xpath('//*[@id="auto-id-1608176486935"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="dologin"]').click()