#与多线程相比，多进程就是import multiprocessing然后替换相应的方法multiprocessing.Process()
from time import sleep,ctime
import multiprocessing

def talk(content,loop):
    for i in range(loop):
        print('Talk:%s %s'%(content,ctime()))
        sleep(2)

def write(content,loop):
    for i in range(loop):
        print('Write:%s %s'%(content,ctime()))
        sleep(2)
process=[]
p1=multiprocessing.Process(target=talk,args=('Hello World!',2))
process.append(p1)
p2=multiprocessing.Process(target=write,args=('Life is short You need Python!',2))
process.append(p2)


if __name__=='__main__':
    for p in process:
        p.start()
    for p in process:
        p.join()
    print("ALL process end! %s"%ctime())