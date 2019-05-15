from selenium import webdriver
from time import sleep
#在百度搜索上传本地图片进行搜索
bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get("http://www.baidu.com")
#定位到百度上传图片的图标
bro.find_element_by_css_selector(".soutu-btn").click()
sleep(2)
#从本地上传图片
bro.find_element_by_css_selector("[value='上传图片']").send_keys('C:\\Users\Public\Pictures\Sample Pictures\\51zxw.png')
sleep(3)
bro.quit()
