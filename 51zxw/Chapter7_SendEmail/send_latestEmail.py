#将最新的测试报告发送至指定邮箱
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import smtplib       #发送邮件模块
from email.header import Header      #定义邮件标题
from email.mime.text import MIMEText #定义邮件内容


def send_email(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()
    #
    smtpserver="smtp.163.com"
    #发送邮箱用户名和密码
    user='xie_xiao_mei@163.com'
    password='1231XXM69'
    #发送和接收邮箱
    sender='xie_xiao_mei@163.com'
    receives=['630906365@qq.com','xiexiaomei@xfzb88.com','2280323531@qq.com']
    #发送邮件主题和内容
    subject="Web Selenium 自动化测试报告"
    #HTML邮件正文
    msg=MIMEText(mail_content,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=sender
    msg['To']=','.join(receives)
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    #HELO向服务器标识用户身份
    smtp.helo(smtpserver)
    #EHLO服务器返回结果确认
    smtp.ehlo(smtpserver)
    #登录邮箱
    smtp.login(user,password)

    print("Start send email......")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("Send end!")

def latest_report(report_dir):
    lists=os.listdir(report_dir)

    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
    print("new report is:"+lists[-1])
    #这里跟视频不一样，和视频中的代码一样的话执行会找不到路径
    file=os.path.join(report_dir,lists[-1])
    #print(file)
    return file

if __name__ == '__main__':

    test_dir='D:\learning\Python_workspace\\51zxw\Chapter6_unittest\Test_baidu\\test_case'
    report_dir='D:\learning\Python_workspace\\51zxw\Chapter6_unittest\Test_baidu\\test_report'

    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'

    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title="Test Report",description="baidu search")
        runner.run(discover)
    f.close()

    latest_report=latest_report(report_dir)
    send_email(latest_report)


