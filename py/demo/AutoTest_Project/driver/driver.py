from selenium import webdriver
#定义浏览器的方法
def browser():
    #firefox浏览器
    driver=webdriver.Firefox()
    #谷歌浏览器
    # driver=webdriver.Chrome()
    #ie浏览器
    # driver=webdriver.Ie()
    #测试各个浏览器是否能正常运行
    # driver.get("http://www.baidu.com")
    #返回测试的地址信息
    return driver
#当前调试运行
if __name__=='__main__':
    browser()