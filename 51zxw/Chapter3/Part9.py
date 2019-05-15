#条件判断
#根据分数来判断学生成绩是否为优秀，80分及以上为优秀，评级为A，成绩80分及以上为A,60-79为B,60以下为C
# score=60
# if score>=80:
#     print("score is A")
# else:
#     print("score is not A")
# score=90
# if score>=80:
#     print("Score is A " )
# elif score>=60:
#     print('Score is B ')
# else:
#     print('Score is C ')






score=[60,56,61,78,80,81,90,91]
for i in range(10):
    if score[i]>=80:
        print("Score is %d"%score[i],"and range is A" )
    elif score[i]>=60:
        print("Score is %d"%score[i],"and range is B")
    else:
        print("Score is %d"%score[i],"and range is C")