# coding=utf-8
from selenium import  webdriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.baidu.com")
try:
    driver.find_element_by_id("form")
    print('test pass:tag name found')
except Exception as msg:
    print("Exception found",format(msg))

