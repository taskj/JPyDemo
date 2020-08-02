from selenium import webdriver

wd = webdriver.Chrome()
#wd = webdriver.Firefox()

wd.get('https://www.baidu.com')

element = wd.find_element_by_id('kw')
element.send_keys("氰化欢乐秀")
element.find_element_by_id('su')
element.click()


