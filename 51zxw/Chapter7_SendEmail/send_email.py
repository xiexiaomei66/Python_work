import smtplib  #发送邮件模块
from email.mime.text import MIMEText #定义邮件内容
from email.header import Header #定义邮件标题
#发送邮箱服务器
smtpserver='smtp.163.com'
#发送邮件用户名密码
user='xie_xiao_mei@163.com'
password='1231XXM69'#授权码，可以在邮箱设置，不是登录密码
#发送和接收邮件的邮箱
sender='xie_xiao_mei@163.com'
receive='630906365@qq.com'
#邮件的标题和内容
subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'
#HTML邮件正文
msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='xie_xiao_mei@163.com'
msg['To']='630906365@qq.com'
#SLL协议端口号要使用465（可以在网上查）
smtp=smtplib.SMTP_SSL(smtpserver,465)
#向服务器标识用户身份
smtp.helo(smtpserver)
#服务器返回确认
smtp.ehlo(smtpserver)
#登录邮箱服务器用户名和密码
smtp.login(user,password)


print("Start send Email......")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("Send Email end!")
