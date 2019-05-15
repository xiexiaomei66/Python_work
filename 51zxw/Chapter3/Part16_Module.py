#Python 模块引用
#import time
# import random
# from time import sleep
# #print(time.ctime())
# num=random.randint(0,100)
# print(num)

#from ... import 从模块中导入指定的部分

# sleep(5)
# print('sleep over')

#3-17 跨目录模块引用
from Part15 import Student
stu1=Student('Jack','Beijing')
stu1.talk()
stu2=Student('Harry','Shanghai')
stu2.talk()
#import搜索路径
# 1、当前目录
# 2、如果不在当前目录，Python则搜索PYTHONPATH下的每个目录
# 3、如果都找不到，Python会查看安装目录默认途径
