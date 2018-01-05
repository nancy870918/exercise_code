
from redmin_locators import LoginPageLocators,LeaveAppLocators
from time import sleep
from datetime import datetime,timedelta

class BasePage():
    def __init__(self,driver):
        self.driver = driver

class LoginPage(BasePage):
    def enter_username(self):
        ele = self.driver.find_element(*LoginPageLocators.username)
        ele.clear()
        ele.send_keys('liangmf')

    def enter_passward(self):
        ele = self.driver.find_element(*LoginPageLocators.password)
        ele.clear()
        ele.send_keys(2)

    def click_login(self):
        ele = self.driver.find_element(*LoginPageLocators.loginsubmit)
        ele.click()

    def get_login_name(self):
        ele = self.driver.find_element(*LoginPageLocators.loginname)
        return ele.text

class Login(BasePage):
    def user_login(self,username='liangmf',password=2):
        "获取用户登录信息,初始化登录帐号"
        self.driver.find_element(*LoginPageLocators.username).clear()
        self.driver.find_element(*LoginPageLocators.username).send_keys(username)
        self.driver.find_element(*LoginPageLocators.password).clear()
        self.driver.find_element(*LoginPageLocators.password).send_keys(password)
        self.driver.find_element(*LoginPageLocators.loginsubmit).click()

class LeavePage(BasePage):
    def enter_leave_butten(self):
        "定位请假申请按钮"
        try:
            leave_ele = self.driver.find_element(*LeaveAppLocators.leave_butten)
            leave_ele.click()
        except Exception as e:
            print('enter_leave_butten not found')


    def enter_leave_type(self):
        "输入请假类型"
        try:
            leave_ele = self.driver.find_element(*LeaveAppLocators.leave_type)
            leave_ele.click()
        except Exception as e:
            print(e)
            return u'请假类型未找到'


    def enter_leave_reason(self):
        "输入请假原因"
        return self.driver.find_element(*LeaveAppLocators.leave_reason).send_keys('测试请假')

    def enter_date_time(self):
        my_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        x = 0
        while my_date:

            # 赋值当前时间给开始时间和结束时间
            self.driver.find_element(*LeaveAppLocators.startdate).clear()
            sleep(1)
            self.driver.find_element(*LeaveAppLocators.enddate).clear()
            sleep(1)
            self.driver.find_element(*LeaveAppLocators.startdate).send_keys(my_date)
            sleep(1)
            self.driver.find_element(*LeaveAppLocators.enddate).send_keys(my_date)
            sleep(1)
            self.driver.find_element(*LeaveAppLocators.LeaveSubmit).click()
            sleep(4)
            self.content = self.driver.find_element(*LeaveAppLocators.LeaveSubmitContent).text
            sleep(4)
            if self.content == '提交成功':
                self.sucess_content = self.content
                break
            else:
                x = x + 1
                my_date = (datetime.now() + timedelta(days=x)).strftime("%Y-%m-%d")










