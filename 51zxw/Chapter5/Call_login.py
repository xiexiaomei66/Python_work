from selenium import webdriver
from time import sleep
from LoginClass import *
#这里的引入会报错，在原文件单击右键--Mark director as--Sources Root
bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get("http://10.68.8.34:18080")
bro.implicitly_wait(10)
Login().user_login(bro)
sleep(3)
Login().user_Logout(bro)
sleep(3)
bro.quit()