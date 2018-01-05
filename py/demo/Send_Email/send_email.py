#发送邮件模块
import smtplib
#定义邮件内容
from email.mime.text import  MIMEText
#定义邮件标题
from email.header import Header

#发送邮箱服务器(需要开启SMTP服务)
smtpserver='smtp.163.com'

#发送邮箱用户名和密码
user='nancy870918@163.com'
password='1993wls'

#发送和接收邮箱
sender='nancy870918@163.com'
receive='wangls@toone.com.cn'

#发送邮件主题和内容
subject='Web Selenium自动化测试报告'
content='<html><h1 style="color:red">测试网络2</h1></html>'

#HTML 邮件正文
msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From'] = sender
msg['To'] = receive

#SSL协议端口号要使用465
smtp=smtplib.SMTP_SSL(smtpserver,465)

#HTLO向服务器标识用户身份
smtp.helo(smtpserver)
#服务器返回结果确认
smtp.ehlo(smtpserver)
#登录邮箱服务器用户名和密码
smtp.login(user,password)

print("开始发送邮件...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("邮件发送完成！")