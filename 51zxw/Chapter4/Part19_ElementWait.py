from selenium import webdriver
from time import sleep,ctime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

br=webdriver.Firefox()
br.get('http://www.baidu.com')
sleep(2)

# #显示等待
# br.find_element_by_css_selector('#kw').send_keys('Selenium')
# #每隔0.5秒去检测一次su元素，最长等待5秒,如果5秒后还没有出现就会抛出异常
# ele=WebDriverWait(br,5,0.5).until(EC.presence_of_element_located((By.ID,'su123')))
# ele.click()
# sleep(3)
# br.quit()


#隐式等待（需要引入NoSuchElementException包）
br.implicitly_wait(10)#隐式等待时间设定5秒(针对脚本中所有的元素最多等待5秒)
#检测搜索框是否存在
try:
    print(ctime())
    br.find_element_by_css_selector("#kw").send_keys('Python')
    br.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())
sleep(3)
br.quit()

