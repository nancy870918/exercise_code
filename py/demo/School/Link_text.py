# coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://www.baidu.com")
# try:
#     driver.find_element_by_link_text("新闻")
#     print('test pass:element found by link text')
# except Exception as msg:
#     print("Exception found",format(msg))


try:
    driver.find_element_by_partial_link_text("主页").click()
    print('test pass:element found by partail link text')
except Exception as msg:
    print("Exception found",format(msg))