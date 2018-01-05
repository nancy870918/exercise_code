# -*- coding: utf-8 -*-
from time import sleep
from Call_Logicpara import *
driver.implicitly_wait(8)
# sleep(5)
# # 截取登录后的系统图片
# driver.get_screenshot_as_file(r"D:\py\python_script\login.jpg")
# sleep(8)

#我的事务
#点击请假申请
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage1') and @class='img-responsive default pull-left']").click()
try:
    #定位查找请假原因的元素
    driver.find_element_by_class_name('JGFormTitle')
    print("请假申请已找到")
    sleep(2)
    driver.find_element_by_class_name('close').click()
except :
    print("请假申请not found ")



#点击加班申请
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage2')]").click()
try:
    # 定位查找加班原因的元素
    driver.find_element_by_class_name('JGFormRequired')
    print("加班申请已找到")
    sleep(2)
    driver.find_element_by_class_name('close').click()
except :
    print("加班申请not found ")


# #加班原因必填填写
# driver.find_element_by_xpath("//*[@name='overtimeReasons']").send_keys("项目加班")
# sleep(5)
# #点击日期控件

#点击出差申请
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage3')]").click()
try:
    #定位查找出差类型的元素
    driver.find_element_by_class_name('JGRadioGroupTitle')
    print("出差申请已找到")
    sleep(2)
    driver.find_element_by_class_name('close').click()
except :
    print("出差申请not found ")



#点击离职申请
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage4')]").click()
try:
    # 定位查找离职类型的元素
    driver.find_element_by_class_name('JGTabControlButtonTopSelected')
    print("离职申请已找到")
    sleep(2)
    driver.find_element_by_class_name('close').click()
except :
    print("离职申请not found ")



#点击调动申请
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage5')]").click()
try:
    # 定位查找调动类型的元素
    driver.find_element_by_class_name('JGTabControlButtonTopSelected')
    print("调动申请已找到")
    sleep(2)
    driver.find_element_by_class_name('close').click()
except :
    print("调动申请not found ")



#点击外出申请
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage6')]").click()
try:
    # 定位查找外出原因的元素
    driver.find_element_by_id('myModalLabel')
    print("外出申请已找到")
    sleep(2)
    driver.find_element_by_class_name('close').click()
except :
    print("外出申请not found ")


Login().user_logout(driver)











