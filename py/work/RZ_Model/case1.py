from time import sleep
from Call_Logicpara import *
from datetime import datetime,timedelta
#我的申请
driver.implicitly_wait(20)


#case1点击请假申请并走流程
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage1') and @class='img-responsive default pull-left']").click()
sleep(2)
try:
    #定位查找请假原因的元素
    apply = driver.find_element_by_xpath("//h4[@id='myModalLabel' and @class='modal-title']").text
    print(apply)
except :
    print("请假申请not exits ")
sleep(1)
driver.find_element_by_xpath("//*[contains(text(),'事假')]").click()  #必填项申请假别选择事假
sleep(1)
driver.find_element_by_xpath("//*[@class='JGFormTextError'and @name='Cause']").send_keys('测试请假') #必填项请假原因
sleep(1)

my_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
x = 0
while my_date:
    print(my_date)
    #赋值当前时间给开始时间和结束时间
    driver.find_element_by_xpath("//input[@id='isc_6V'and @name='startDate']").clear()
    driver.find_element_by_xpath("//input[@id='isc_76'and @name='endDate']").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id='isc_6V'and @name='startDate']").send_keys(my_date)
    sleep(1)
    driver.find_element_by_xpath("//input[@id='isc_76'and @name='endDate']").send_keys(my_date)
    sleep(1)
    driver.find_element_by_xpath("//*[contains(text(),'提交')]").click()
    sleep(4)
    content = driver.find_element_by_xpath("//div[@id='dialog_content_div'and @class='content']").text
    sleep(4)
    if content =='提交成功':
        print('请假申请流程成功')
        break
    else:
        x = x + 1
        my_date = (datetime.now() + timedelta(days=x)).strftime("%Y-%m-%d")

sleep(2)

#case2 加班申请并走流程
driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage2')]").click()
try:
    # 定位查找加班原因的元素
    driver.find_element_by_class_name('JGFormRequired')
    print("加班申请已找到")
except :
    print("加班申请not found ")

sleep(1)
driver.find_element_by_xpath("//*[@class='JGFormTextError'and @name='overtimeReasons']").send_keys('项目加班') #必填项
sleep(1)
my_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
sleep(1)
driver.find_element_by_xpath("//input[@id='isc_7O'and @name='startDate']").clear()
driver.find_element_by_xpath("//input[@id='isc_7D'and @name='endDate']").clear()
sleep(1)
driver.find_element_by_xpath("//input[@id='isc_7O'and @name='startDate']").send_keys(my_date)
sleep(1)
driver.find_element_by_xpath("//input[@id='isc_7D'and @name='endDate']").send_keys(my_date)
sleep(1)
driver.find_element_by_xpath("//*[contains(text(),'提交')]").click()
sleep(4)
print('加班申请流程成功')
