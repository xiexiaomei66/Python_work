#coding:utf-8
#数组元素的增减
#末尾添加元素
student=['Jack','Bob','Harry','Micle']
student.append('Jane')
print(student)
#指定位置添加元素
student.insert(0,'Moona')#在第一个前插入
print(student)
#修改元素
student[0]='Number'#将第一个元素替换掉
print(student)
#删除最后一个元素
student.pop()
print(student)
#删除指定元素
student.pop(1)#删除角标为1的元素
print(student)