"""
讲所有元素，按页面保存在不同的class下面
"""
from selenium.webdriver.common.by import By

class LoginPageLocators():
    username = (By.XPATH,"//input[@widgetcode='JGTextBox1']") #用户名
    password = (By.XPATH,"//input[@widgetcode='JGPasswordBox1']") #密码
    loginsubmit = (By.XPATH,"//*[@widgetcode='JGButton1']") #登录
    loginname = (By.XPATH,"//span[contains(text(),'登录时间')] ") #登录后的内容显示

class LeaveAppLocators():
    leave_butten = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage1') and @class='img-responsive ']") #请假申请
    # Leave_Context = (By.XPATH,"//h4[@id='myModalLabel' and @class='modal-title']")#判读获取的请假申请按钮内容
    leave_type = (By.XPATH,"//*[contains(text(),'事假')]")  #必填项申请假别选择事假
    leave_reason = (By.XPATH,"//*[@class='JGFormTextError'and @name='Cause']") #必填项请假原因
    startdate = (By.XPATH,"//input[@id='isc_6V'and @name='startDate']") #开始时间
    enddate = (By.XPATH,"//input[@id='isc_76'and @name='endDate']")#结束时间
    LeaveSubmit = (By.XPATH,"//*[contains(text(),'提交')]")#请假提交按钮
    LeaveSubmitContent = (By.XPATH,"//div[@id='dialog_content_div'and @class='content']")#请假申请提交提示框内容