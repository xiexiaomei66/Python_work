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

def test_user_login(driver,username,password):
    login_page=LoginPage(driver)
    login_page.open()



    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()



