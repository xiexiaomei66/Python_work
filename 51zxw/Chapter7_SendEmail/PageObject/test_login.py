from LoginPage import *
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()

username='13662673315'
password='111111'

test_user_login(driver,username,password)
sleep(3)
driver.quit()