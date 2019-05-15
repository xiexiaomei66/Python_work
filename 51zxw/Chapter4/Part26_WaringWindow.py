from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#点击百度首页设置按钮，然后弹出警告窗口进行相关处理
br=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
br.get("http://www.baidu.com")
br.maximize_window()
br.find_element_by_link_text("设置").click()
sleep(2)
br.find_element_by_link_text("搜索设置").click()
sleep(2)
#br.find_element_by_link_text("保存设置").click()
br.find_element_by_link_text("恢复默认").click()
sleep(2)
#处理警告窗
alert=br.switch_to_alert()
alert.accept()
sleep(2)
br.quit()