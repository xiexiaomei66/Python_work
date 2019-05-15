from selenium import webdriver
from time import sleep,ctime
#分别打开我要自学网页面和百度页面，然后进行截图
bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get('http://www.51zxw.net')
bro.maximize_window()
#对我要自学网页面截图
bro.get_screenshot_as_file(r"D:\谢小妹\我的学习资料\python+selenium_51zxw\screenshoot\51zxw.jpg")
sleep(2)
bro.get('http://www.baidu.com')
bro.get_screenshot_as_file(r'D:\谢小妹\我的学习资料\python+selenium_51zxw\screenshoot\baidu.png')
#bro.get_screenshot_as_file(r'D:\谢小妹\我的学习资料\python+selenium_51zxw\screenshoot\baidu%s.png'%ctime().strftime("%Y%m%d.%H%M%S.%f"))
sleep(2)
bro.quit()