from time import sleep
from multiprocessing import Process
import os

def task1():
    while(True):
        sleep(1)
        print('This is task1......',os.getpid(),os.getppid())


def task2():
    while(True):
        sleep(2)
        print('This is task2......',os.getpid(),os.getppid())

number=1
if __name__ == "__main__":
    # 子进程，主进程运行完，开始子进程
    p=Process(target=task1,name='任务1')
    p.start()
    print(p.name)
    p1=Process(target=task2,name='任务2')
    p1.start()
    print(p1.name)

    while(True):
        number+=1
        sleep(0.2)
        if number==50:
            p.terminate()
            p1.terminate()
            break
        else:
            print('---------number:',number)

    print('---------')
    print('*********')