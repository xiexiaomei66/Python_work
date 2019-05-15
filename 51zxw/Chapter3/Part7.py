#元组
#元组与数组类似，不同之处在于元组的元素一旦定义就不能使用方法将其进行增删改。元组使用小括号，数组使用方括号
# course=('Chiness','Math','English','Computer')
# print(course)
# print(course[0])
# print(course[-1])
# print(course[1:3])#前包后不包
# print(course[1:])
# print(course[:2])
# print(len(course))#元组的长度
#要定义一个只有1个元素的元组，则需要在元素后面加逗号，用来消除数学歧义,如果不加逗号会认为是赋值
#t=(1,)
#返回元组最大的值
score=(78,90,88,67,78)
maxScore=max(score)
print(maxScore)