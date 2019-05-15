from selenium import webdriver
from time import sleep

#打开我要自学网Selenium课程主页，然后打开2-1课程详情页，再回到课程主页打开3-1课程详情页
br=webdriver.Firefox()
#打开Selenium课程页面
br.get("https://www.51zxw.net/list.aspx?cid=615")
#获取课程主页的窗口句柄(调用方法)
selenium_index=br.current_window_handle
sleep(2)
#点击2-1课程链接，进入课程详情页面
br.find_element_by_partial_link_text('2-1').click()
sleep(4)
#跳转到课程主页窗口，点击3-1
br.switch_to.window(selenium_index)
sleep(3)
br.find_element_by_partial_link_text('3-1').click()
sleep(3)
br.quit()
