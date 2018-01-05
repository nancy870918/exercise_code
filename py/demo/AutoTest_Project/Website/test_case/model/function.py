from selenium import webdriver
import os
#发送邮件模块
import smtplib
#定义邮件内容
from email.mime.text import  MIMEText
#定义邮件标题
from email.header import Header
#定义一个截图路径的方法
def insert_img(driver,filename):
    #动态获取function截图路径
    fun_path=os.path.dirname(__file__)
    # print(fun_path)

    #获取testcase路径
    base_dir=os.path.dirname(fun_path)
    # print(base_dir)
    #将路径转化为字符串
    base_dir=str(base_dir)
    #对路径的字符串进行替换
    base_dir=base_dir.replace('\\','/')
    # print(base_dir)
    #以website做切割,读取第一个元素（获取项目文件的根目录路径）
    base=base_dir.split('/Website')[0]
    print(base)
    #指定截图存放路径
    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

#查找最新的测试报告
def latest_report(report_dir):
    lists=os.listdir(report_dir)
    #print(lists)
    lists.sort(key=lambda fn:os.path.getatime(report_dir + '\\'+ fn))
    file=os.path.join(report_dir,lists[-1])
    #print(file)
    return file

#将测试报告发送到邮件
def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()
    # 发送邮箱服务器(需要开启SMTP服务)
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名和密码
    user = 'nancy870918@163.com'
    password = '1993wls'
    # 发送和接收邮箱
    sender = 'nancy870918@163.com'
    receives =[ 'wangls@toone.com.cn','chenyc@toone.com.cn']
    # 发送邮件主题
    subject='Web Selenium 自动化测试报告'
    # HTML 邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)
    # SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # HTLO向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("开始发送邮件...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("邮件发送完成！")

if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver,'sougou.jpg')
    driver.quit()