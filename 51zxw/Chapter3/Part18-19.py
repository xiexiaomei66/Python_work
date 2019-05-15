#Python 异常
#异常类型
#FileNotFoundError找不到指定文件的异常
#NameError未声明、初始化对象（没有属性 ）
#BaseException所有异常的基类
# try:
#     fileName=input('please input fileName:')
#     open('%s.txt'%fileName)
# except FileExistsError:
#     print('%s.txt file not found'%fileName)
# try:
#     stu='jack'
#     print(stu)
# except NameError:
#     print('stu not define')

#try:
    #stu='jack'
    #print(stu)
#except BaseException:
    #print('stu not define')

#系统自带的异常报错
# try:
#     print(stu)
# except BaseException as msg:
#     print(msg)
#可以加else
# try:
#     stu='jack'
#     print(stu)
# except BaseException as msg:
#     print(msg)
# else:
#     print('stu is define')

#可以加finally
# try:
#     stu='jack'
#     print(stu)
# except BaseException as msg:
#     print(msg)
# else:
#     print('stu is define')
# finally:
#     print('The end!')
#前面try语句是执行过程中捕获代码块的异常，而raise是通过事先定义一个条件，一旦符合异常条件就抛出异常
#raise只能用于Python标准异常类

def division(x,y):
    if y==0:
        raise ZeroDivisionError('Zero is not allow!')
    return x/y
try:
    division(8,0)
except BaseException as msg:
    print(msg)