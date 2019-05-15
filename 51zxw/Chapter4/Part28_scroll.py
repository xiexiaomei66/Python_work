from selenium import webdriver
from time import sleep
#打开我要自学网页面，然后将滚动条拖到最底部
bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get('http://www.51zxw.net')
sleep(2)
bro.maximize_window()
sleep(2)
#将滚动条拖到最底部
js='var action=document.documentElement.scrollTop=10000'
bro.execute_script(js)
sleep(5)

#将滚动条拖到最顶部
vs='var action=document.documentElement.scrollTop=0'
bro.execute_script(vs)
sleep(2)
bro.quit()







