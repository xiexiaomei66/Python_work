from selenium import webdriver
from time import sleep
#bro,username,password三个都是参数
class Login():
    def user_login(self,bro,username,password):
        sleep(2)
        bro.find_element_by_css_selector('#loginNow').click()
        sleep(2)
        #先将输入框内容清干净
        bro.find_element_by_css_selector('[nullmsg="请输入用户名"]').clear()
        sleep(2)
        #输入用户名
        bro.find_element_by_css_selector('[nullmsg="请输入用户名"]').send_keys(username)
        bro.find_element_by_name('paramMap.password').clear()
        bro.find_element_by_name('paramMap.password').send_keys(password)
        sleep(2)
        bro.find_element_by_id('btn_login_per').click()
    def user_Logout(self,bro):
        bro.find_element_by_partial_link_text('安全退出').click()