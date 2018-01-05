from selenium import webdriver

def isElementExist(ele):
        if ele:
                print("菜单已找到")
        else:
                print("菜单not exist")

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    try:
        driver.find_element_by_xpath(" //input1")
        ele = 1
    except:
        ele = 0
    a = isElementExist(ele)

