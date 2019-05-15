from selenium import webdriver
from datetime import datetime
import os
from email.mime.text import  MIMEText
import smtplib
from email.header import Header

def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    print(func_path)

    base_dir=os.path.dirname(func_path)
    print(base_dir)

    base_dir=str(base_dir)
    #字符串的转化
    base_dir=base_dir.replace('\\','/')

    print(base_dir)
    #以Website为拆分点拆分列表
    base=base_dir.split('/Website')[0]
    print(base)
    #文件路径的拼接
    time=datetime.now().strftime("%Y%m%d.%H%M%S.%f")
    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

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
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver,'baidu.png')