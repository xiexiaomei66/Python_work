#coding:utf-8
import csv

#3-21 读取txt文件
# f=open('stu_info.txt','r')
# lines=f.readlines()
# print(lines)
# for line in lines:
#     print(line.split(',')[0])#对指定的符号进行分割（0是表示对第一个元素分割，前后截断)


#3-22 csv文件读写

# csv_file=csv.reader(open('stu_info.csv','r'))
# print(csv_file)#打印的是一个地址
# for stu in csv_file:
#     print(stu)
#csv文件写入
#对stu_info.csv文件追加写入两个学生的信息Marry和Rom
stu = ['Marry',28,'Changsha']
stu1=['Rom',23,'Chengdu']
#打开文件，写入前要先关闭改文档，不然会报错无权限写入
add=open('stu_info.csv','a',newline='')#不加newline=‘’的话，会插入空行
#设定写入模式
csv_write=csv.writer(add,dialect='excel')
#写入具体内容，在后面追加
csv_write.writerow(stu)
csv_write.writerow(stu1)
print('Write file over!')
Afteradd=open('stu_info.csv','r')
for stu in Afteradd:
    print(stu)
