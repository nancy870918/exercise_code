import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #用于传送附件
#发送邮箱服务器
smtpserver='smtp.163.com'
#发送邮箱用户名密码
user='nancy870918@163.com'
password='1993wls'
#发送和接收邮箱
sender='nancy870918@163.com'
receive=['wangls@toone.com.cn','chenyc@toone.com.cn']
#发送邮件主题和内容
subject='Web Selenium 附件发送测试'
content='<html><h1 style="color:red">我要自学网！</h1></html>'
#构造附件内容

