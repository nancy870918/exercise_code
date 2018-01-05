# coding=utf-8
import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(2)
ele_string=driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a").text
if(ele_string==u"Python"):
    print ("测试成功")
driver.quit()