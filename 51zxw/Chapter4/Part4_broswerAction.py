from selenium import webdriver
from time import sleep


broswer=webdriver.Firefox()
broswer.get("https://www.51zxw.net")
broswer.maximize_window()#页面最大化
sleep(2)
broswer.get('https://www.51zxw.net/list.aspx?cid=615')
broswer.set_window_size(400,800)
broswer.refresh()#刷新
sleep(2)

broswer.back()#后退
sleep(2)

broswer.forward()#前进
sleep(2)

broswer.quit()
