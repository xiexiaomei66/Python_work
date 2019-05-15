#打开百度首页，在搜索框自动输入“Selenium我要自学网”关键字，然后点击搜索按钮，查看搜索页面
from selenium import webdriver
from time import sleep
broswer=webdriver.Firefox()


#id、name定位
# broswer.get('https://www.baidu.com')
# broswer.maximize_window()
# sleep(2)
# broswer.find_element_by_name('wd').send_keys('Selenium我要自学网')
# #broswer.find_element_by_id('kw').send_keys('Selenium我要自学网')
# sleep(2)
# broswer.find_element_by_id('su').click()
# sleep(3)
# broswer.quit()


#tag_name定位
# 定位标签名为input的元素（从头开始第一个input）
# broswer.get('http://www.51zxw.net')
# sleep(2)
# broswer.find_element_by_id('frm_login_url').click()
# sleep(2)
# broswer.find_elements_by_tag_name('input')[0].send_keys('792392967@qq.com')
# #获取所有的input中的第一个,
# # 一般不建议使用tag_name定位，因为一个页面中相同的标签名字会有很多，很不方便
# broswer.find_element_by_name('pwd').send_keys('jwx569716')
# sleep(3)
# broswer.quit()

#class_name定位
# broswer.get('http://www.baidu.com')
# broswer.maximize_window()
# broswer.find_element_by_class_name('s_ipt').send_keys('Selenium')
# sleep(3)
# broswer.find_element_by_id('su').click()
# sleep(2)
# broswer.refresh()
# broswer.get('https://www.youyadai.cn/')
# sleep(2)
# broswer.find_element_by_id('loginNow').click()
# sleep(2)
# broswer.find_element_by_id('email').send_keys('13662673315')
# broswer.find_element_by_name('paramMap.password').send_keys('111111')
# sleep(2)
# broswer.find_element_by_class_name('login_btn').click()
# sleep(15)
# broswer.back()
# sleep(2)
# broswer.forward()
# sleep(5)
# broswer.quit()


#link_text定位（就是根据超链接文字进行定位）
# broswer.get('http://www.51zxw.net')
# broswer.maximize_window()
# broswer.find_element_by_link_text('程序开发').click()
# sleep(2)
# # js="var q=document.getElement.scrollTop=10000"
# # broswer.execute_script(js)
# broswer.find_element_by_partial_link_text('SQL').click()#部分截取字段，取的字段应该也是唯一的
# sleep(2)
# broswer.quit()


#Xpath定位---绝对与相对定位(Xpath基于XML的树状结构，提供在数据结构树中找寻节点的能力)
# broswer.get('http://www.baidu.com')
# #绝对路径定位,单击右键复制xpath（缺点：一旦路径中的某个路径有调整，就会查找不到该路径了）
# #broswer.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/form/span[1]/input").send_keys('51zxw')
# #broswer.find_element_by_xpath("//*[@class='s_ipt']").send_keys('51zxw')
# #利用元素熟悉定位--定位到input标签中为kw的元素
# #broswer.find_element_by_xpath("//input[@id='kw']").send_keys('Selenium')
# #定位input标签中name属性为wd的元素
# #broswer.find_element_by_xpath("//input[@name='wd']").send_keys('Selenium')
# #定位所有标签元素中，class属性为s_ipt的元素(如有多个class相同，*应该要指定标签)
# broswer.find_element_by_xpath("//*[@class='s_ipt']").send_keys('Selenium')
# broswer.find_element_by_id('su').click()
# sleep(3)
# broswer.quit()


#Xpath层级与逻辑组合定位
# broswer.get("http://51zxw.net")
# broswer.maximize_window()
# sleep(2)
# broswer.find_element_by_link_text("登录").click()
# sleep(2)
# #层级和属性结合定位--自学网首页输入用户和密码(input的角标是从1开始)
# broswer.find_element_by_xpath("//form[@id='loginFrom']/div[1]/div[2]/input[1]").send_keys('792392967@qq.com')
# sleep(2)
# broswer.find_element_by_xpath("//form[@id='loginFrom']/div[1]/div[4]/input[2]").send_keys('jwx569716')

#逻辑运算组合定位（属性不唯一的问题可以用这个来解决）
#同时使用class和name来定位（//表示当前页面）
# broswer.find_element_by_xpath("//input[@class='input-text size-L radius icon' and @name='loginStr']").send_keys("792392967@qq.com")
# broswer.find_element_by_xpath("//input[@id='pwd' and @name='pwd']").send_keys("jwx569716")
# sleep(3)
# broswer.quit()


#Css定位
# broswer.get("http://www.baidu.com")
#根据id定位
# broswer.find_element_by_css_selector('#kw').send_keys('Selenium 我要自学网')
# #根据class定位
# broswer.find_element_by_css_selector('.s_ipt').send_keys('Selenium 我要自学网')
# #通过属性定位
# broswer.find_element_by_css_selector('[autocomplete="off"]').send_keys('Selenium 我要自学网')
# sleep(2)
# broswer.find_element_by_id('su').click()


broswer.get("http://www.51zxw.net")
broswer.find_element_by_link_text("登录").click()
sleep(2)
#通过元素层级来定位
broswer.find_element_by_css_selector("form#loginFrom>div[1]>div[2]>input[type='text']").send_keys('13662673315')
sleep(5)
broswer.quit()