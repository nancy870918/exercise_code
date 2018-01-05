import yaml
from selenium import webdriver
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = 'smtp.163.com'
sender = 'nancy870918@163.com'
passwd = '1993wls'
receiver = 'wangls@toone.com.cn'

msg = MIMEMultipart()
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = '主题'
msg.attach(MIMEText('邮件正文'))

# att1 = MIMEText(open('test1.xls','rb').read(),'base64','utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="testresult.xls"'
# msg.attach(att1)

try:
    smtpobj = smtplib.SMTP(host,port=25)
    smtpobj.login(sender,passwd)
    smtpobj.sendmail(sender,receiver,msg.as_string())
    smtpobj.quit()
    print('send success')
except:
    print('send err')