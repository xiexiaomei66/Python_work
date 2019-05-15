from selenium import webdriver
from time import sleep
from LoginClass_param import *
driver=webdriver.Chrome()
driver.get('http://10.68.8.34:18080')
driver.set_window_size(2000,1000)
driver.implicitly_wait(10)
Login().user_login(driver,"13662673315","111111")
sleep(3)
Login().user_Logout(driver)

Login().user_login(driver,"15100000010","111111")
sleep(3)
Login().user_Logout(driver)
sleep(2)
driver.quit()