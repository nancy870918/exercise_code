
from  selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__userName']").send_keys(1)
# try:
#     driver.find_element_by_id("kw")
#     print("test pass:ID found")
# except Exception as msg:
#     print("Exception found",format(msg))