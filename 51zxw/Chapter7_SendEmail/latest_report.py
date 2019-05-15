#获取目录下的最新测试报告
import os #用于访问操作系统功能的模块

#测试报告存放的位置
report_dir='D:\learning\Python_workspace\\51zxw\Chapter6_unittest\Test_baidu\\test_report'
#os.listdir()方法用于返回指定的文件夹包含的文件或者文件夹名字的列表
lists=os.listdir(report_dir)

#按时间顺序对该目录下文件夹下面的文件进行排序
lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
print(lists)
print("latest report is:"+lists[-1])

#输出最新报告的路径
file=os.path.join(report_dir,lists[-1])
print(file)


