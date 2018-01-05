import unittest #导入unittest模块
from driver import *  #导入driver模块，读取浏览器
#封装用例开始结束的类
class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

