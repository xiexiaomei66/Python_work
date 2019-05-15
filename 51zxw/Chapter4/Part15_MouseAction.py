from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

bro=webdriver.Firefox()
bro.get('http://www.baidu.com')
bro.maximize_window()
sleep(2)

bro.find_element_by_css_selector('#kw').send_keys('Python')
element=bro.find_element_by_css_selector('#kw')
sleep(2)
#双击操作
ActionChains(bro).double_click(element).perform()
sleep(2)
#点击右击鼠标
ActionChains(bro).context_click(element).perform()
sleep(2)
#鼠标悬停
above=bro.find_element_by_css_selector('.pf')
ActionChains(bro).move_to_element(above).perform()
sleep(5)
bro.quit()
