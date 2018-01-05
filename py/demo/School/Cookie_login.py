from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://10.1.30.32:8081/module-operation!executeOperation?componentCode=vp_hr_recruitment_web&windowCode=login&token=%7B%22data%22%3A%7B%22inputParam%22%3A%7B%22variable%22%3A%7B%22v3ComponentTitle%22%3Anull%7D%7D%7D%7D")

#手动添加cookie
driver.add_cookie({'name':'JSESSIONID','value':'1i6kg2p81mo8b13g1z0l919wd0'})
driver.add_cookie({'name':'v_userAccount','value':'U2FsdGVkX1%2B7Gr9qyxq%2Bxa2PpS2cLoqZ3AZcCKTBOys%3D'})
driver.add_cookie({'name':'v_userPwd','value':'U2FsdGVkX1%2BWFiQv2NTzi70s0Mwv0VhbUdq16u6zsqM%3D'})


sleep(2)
driver.refresh()
sleep(3)
# driver.quit()
