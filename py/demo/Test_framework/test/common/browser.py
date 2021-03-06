import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH,REPORT_PATH

#可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox':webdriver.Firefox,'chrome':webdriver.Chrome,'ie':webdriver.Ie,'phantomjs':webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox':'wires','chrome':CHROMEDRIVER_PATH,'ie':IEDRIVER_PATH,'phantomjs':PHANTOMJSDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

#根据传入的参数选择浏览器的driver去打开对应的浏览器
class Browser(object):
    def __int__(self,browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!'%','.join(TYPES.keys()))
        self.driver = None

    def get(self,url,maximize_window=True,implicitly_wait=30):
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

#保存截图的方法，可以保存png截图到report目录下
    def save_screen_shot(self,name='screen_shot'):
        day = time.strftime('%Y%m%d',time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s'% day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S',time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png'%(name,tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()