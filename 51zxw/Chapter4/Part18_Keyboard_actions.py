from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

bro=webdriver.Chrome(executable_path = 'C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get("http://www.baidu.com")
bro.maximize_window()
bro.find_element_by_css_selector('#kw').send_keys("Python")
sleep(2)
#全选Ctrl+a
bro.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
sleep(2)
#复制Ctrl+c
#bro.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
#剪切Ctrl+x
bro.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'x')
sleep(2)
bro.get("http://www.sohu.com")
sleep(2)
#粘贴Ctrl+v
bro.find_element_by_css_selector('[type="text"]').send_keys(Keys.CONTROL,'v')
sleep(2)
bro.find_element_by_css_selector('.search-btn').click()
sleep(2)
bro.quit()