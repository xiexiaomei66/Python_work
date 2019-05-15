from selenium import webdriver
from time import sleep
#加载浏览器驱动,将驱动放在安装python的根目录下就不需要加驱动路径了
#broswer=webdriver.Chrome(executable_path = 'C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
broswer=webdriver.Firefox()
#broswer=webdriver.Ie()#这个需要在IE的属性---安全页签中的“选择一个区域以查看或更改安全设置”所有的项目的“启用保护模式”勾勾去掉才能驱动
#打开测试环境的网页和百度的首页并打印title后关闭网页
broswer.get("https://www.youyadai.cn/login.do")
broswer.maximize_window()#页面最大化
print(broswer.title)
sleep(5)

broswer.get('http://www.baidu.com')
print(broswer.title)
sleep(5)
broswer.quit()