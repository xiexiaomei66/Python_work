#字典
#字典是另一种可变容器模型，且可存储任意类型对象。字典的每个键值（key=>value）对用
#冒号（:）分割，每个对之间用逗号分割，整个字典包括在花括号中，格式如下所示
#d = {key1:value1,key2:value2}
#键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的
#定义访问字典
student={1:'Jack',2:'Bob',3:'Mary',4:'Micle'}
print(student[3])
#添加元素，添加新的键值对
student[5]='Jane'
print(student)

#修改字典
student[2]='Harry'
print(student)
#删除字典
del student[1]
print(student)

#清空字典全部内容
student.clear()
print(student)
#删除字典
del student
print(student)#已经删除了，打印会报错

