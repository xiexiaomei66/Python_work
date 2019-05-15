from time import ctime,sleep
import threading
#学生同时进行说与写的操作，相当于并联
def talk(content,loop):#content 是定义要说的内容，loop是定义一个循环次数
    for i in range(loop):
        print('Start Talk %s %s '%(content,ctime()))
        sleep(3)
def write(content,loop):
    for i in range(loop):
        print('Start Write %s %s'%(content,ctime()))
        sleep(3)

#将上面两个定义装载到线程
threads=[]

t1=threading.Thread(target=talk,args=('Speak:Hello World!',3))
threads.append(t1)
t2=threading.Thread(target=write,args=('Write:Life is short You need Python!',3))
threads.append(t2)

#执行多线程
if __name__=='__main__':
    for t in threads:
        t.start()    #线程开始
    for t in threads:
        t.join()     #确保所有线程结束后才让整个运行结束
        print("All threads End %r"%ctime())