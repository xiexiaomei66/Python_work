from BasePage import *
from selenium.webdriver.common.by import By
class LoginPage(Page):
    #首页登录
    url='/login.do'

    username_loc=(By.NAME,'paramMap.email')
    password_loc=(By.NAME,'paramMap.password')
    submit_loc=(By.ID,'btn_login_per')

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    loginPass_loc=(By.LINK_TEXT,'账户总览')
    loginFail_loc=(By.NAME,'paramMap.email')

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text
    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text