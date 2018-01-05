#coding=utf-8
from selenium import webdriver
import re
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://home.baidu.com/contact.html")
#得到页面源代码
doc = driver.page_source
#利用正规，找出XXX＠XXX．XXX的字段，保持到emails列表
emails = re.findall(r'[\w]+@[\w.]+',doc)
#循环打印匹配的邮箱
for email in emails:
    print(email)