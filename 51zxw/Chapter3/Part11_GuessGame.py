#生成一个指定范围的随机数（如1-100），然后玩家输入数值猜答案，屏幕会根据玩家输入的数字给出大小提示，一直到玩家猜出准确答案则游戏结束
#1、生成随机数
#2、玩家输入数值
#3、判断大小
#输入答案正确，游戏结束
#输入答案错误，继续提示玩家输入
import random
answer=random.randint(1,100)
n=(int)(input('please input a number(1-100)'))
while n!=answer:
    if n>answer:
        n=(int)(input('数字大了，请重新输入(1-100)'))
    elif n<answer:
        n=(int)(input('数字小了，请重新输入(1-100)'))
print('恭喜你答对了，游戏结束')
