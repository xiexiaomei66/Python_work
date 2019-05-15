import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        '''username and password is normal'''
        print('test_login1_normal is start test...')
        po=LoginPage(self.driver)
        po.Login_action('13662673315',111111)
        sleep(2)
        self.assertEqual(po.type_loginPass_hint(),'账户总览')
        function.insert_img(self.driver,"test_login1_normal.jpg")
        print("test_login1_normal test end!")

    def test_login2_pwdError(self):
        '''username is ok,password is error'''
        print("teat_login2_pwdError is start test...")
        po=LoginPage(self.driver)
        po.Login_action('13662673315',123456)
        sleep(2)
        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"teat_login2_pwdError.jpg")
        print("test_login2_pwdError test end")

    def test_login3_empty(self):
        '''username and password are empty'''
        print("test_login2_empty is start test...")
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(2)
        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"test_login3_empty.jpg")
        print("test_login3_empty test end")

if __name__ == '__main__':
    unittest.main()

