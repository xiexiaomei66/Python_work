from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
bro.get("http://www.baidu.com/")
bro.maximize_window()
bro.implicitly_wait(5)

bro.find_element(By.ID,"kw").clear()
bro.find_element(By.NAME,"wd").send_keys('Selenium')
bro.find_element(By.CLASS_NAME,'s_ipt').send_keys("自学网")
bro.find_element(By.CSS_SELECTOR,'#kw').send_keys("Python")

sleep(3)
bro.find_element(By.ID,'su').click()