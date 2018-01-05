
from Call_Logicpara import *
from time import sleep
driver.implicitly_wait(4)
#增加判断简历菜单是否存在
menu = driver.find_element_by_xpath("//span[@class='con_title title' and text()='简历']").text
if menu == "简历":
    print("简历菜单exist")

    # 点击一级菜单简历，加载二级菜单列表
    driver.find_element_by_xpath("//span[@class='con_title title' and text()='简历']").click()
    sleep(2)
    # 查找二级菜单路径然后定义一个eles变量为list
    eles = driver.find_elements_by_xpath("//*[@class='sub-menu']/li/a/span")

    # 定义一个空列表，用来存储页面中存在的菜单文本
    lst1 = []

    # 循环读取找到的菜单元素
    for ele in eles:
        # 把元素的文本存到列表中
        lst1.append(ele.text)
    print(lst1)

    # 定义一个列表，用来存储预期的所有菜单文本
    lst2 = ["个人基础信息", "家庭状况", "教育经历", "培训经历", "工作经历", "相关信息", "原工作单位薪资情况", "附件管理"]

    for a in lst2:
        if a in lst1:
            print("{} exist".format(a))
        else:
            print("{} not exist ".format(a))
else:

    print("简历菜单not exist")

Login().user_logout(driver)