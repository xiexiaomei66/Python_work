from selenium import webdriver
from time import sleep
bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get('http://www.baidu.com/')
#百度登录已改版不可登陆
bro.add_cookie({'name':'BAIDUID','value':''})
bro.add_cookie({'name':'BDUSS','value':' '})
sleep(3)
bro.refresh()
sleep(3)
bro.quit()