from selenium import webdriver
from time import sleep

#查看访问我要自学网时的Cookies内存
bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get('http://www.51zxw.net')
bro.maximize_window()
#获取cookies全部内容
cookie=bro.get_cookies()
#打印全部的cookie信息
print(cookie)
#打印cookie第一组信息
print(cookie[0])
#添加cookie
bro.add_cookie({'name':'51zxw','value':'www.51zxw.net'})
#打印出所有cookies
for cookie in bro.get_cookies():
    print('%s--%s'%(cookie['name'],cookie['value']))

bro.quit()