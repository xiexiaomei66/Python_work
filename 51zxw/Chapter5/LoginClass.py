from selenium import webdriver
from time import sleep

class Login():
    def user_login(self,bro):
        sleep(2)
        bro.find_element_by_css_selector('#loginNow').click()
        sleep(2)
        #先将输入框内容清干净
        bro.find_element_by_css_selector('[nullmsg="请输入用户名"]').clear()
        sleep(2)
        #输入用户名
        bro.find_element_by_css_selector('[nullmsg="请输入用户名"]').send_keys('15100000010')
        bro.find_element_by_name('paramMap.password').clear()
        bro.find_element_by_name('paramMap.password').send_keys('111111')
        sleep(2)
        bro.find_element_by_id('btn_login_per').click()
    def user_Logout(self,bro):
        bro.find_element_by_partial_link_text('安全退出').click()


if __name__=='__main__':
#在测试环境登录和退出
    bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    bro.get('http://10.68.8.41:18080/')
    bro.maximize_window()
    bro.implicitly_wait(10)
    Login().user_login(bro)
    sleep(2)
    Login().user_Logout(bro)
    sleep(2)
    bro.quit()
