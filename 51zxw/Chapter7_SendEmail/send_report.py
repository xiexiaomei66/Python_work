import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #用于传送附件

#将附件发送到指定邮箱
#发送邮件服务器
smtpserver='smtp.163.com'

#发送邮箱用户名和密码
user='xie_xiao_mei@163.com'
password='1231XXM69'

#发送邮箱和接收邮箱
sender='xie_xiao_mei@163.com'
receives=['xiexiaomemi@xfzb88.com','2280323531@qq.com','630906365@qq.com']

#发送邮件主题和内容
subject='Web Selenium附件发送测试'
content='<html><h1 style="color:red" ></h1></html>'

#构建附件内容'base64',
send_file=open(r"D:\learning\Python_workspace\51zxw\Chapter6_unittest\Test_baidu\test_report\2019-05-06 20_59_08result.html",'rb').read()

att=MIMEText(send_file,'base64','utf-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment;filename="2019-05-06 20_59_08result.html"'

#构建发送与接收信息
msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)

#SSL协议端口号要用465
smtp=smtplib.SMTP_SSL(smtpserver,465)

#HELO向服务器标识用户身份
smtp.helo(smtpserver)
#向服务器返回结果确认
smtp.ehlo(smtpserver)
#登录邮箱服务器用户名密码
smtp.login(user,password)

print('Start send email......')
smtp.sendmail(sender,receives,msgRoot.as_string())

smtp.quit()
print("Send End!")