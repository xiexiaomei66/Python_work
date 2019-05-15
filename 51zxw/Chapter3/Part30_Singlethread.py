from time import ctime,sleep
#先说后写，相当于串联
def talk():
    print('Start talk %r'%ctime())
    sleep(2)
def write():
    print('Start write %r'%ctime())

if __name__=='__main__':#表示如果当前模块是被直接运行的，则该语句之后代码块被运行，如果模块是被导入的，则代码块不被运行

    talk()
    write()
    print('All end! %r'%ctime())