from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

bro=webdriver.Firefox()
bro.get("Http://www.51zxw.net")
sleep(2)
#由于我要自学网改版，页面已经没有这个功能了，没法验证
bro.find_element_by_tag_name("option")[1].click()
bro.find_element_by_css_selector("[value='2']").click()
sleep(2)

#使用Select类定位
select=Select(bro.find_element_by_css_selector("[name='CookieDate']"))#包含了选项框里面的所有元素
select.select_by_index(2)
select.select_by_visible_text("留一年")
select.select_by_value(1)
sleep(2)
bro.quit()