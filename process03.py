from multiprocessing import Process
import time
import os

x=100          # 主进程的x=100
def task():
    global x
    x=0        # 子进程的x=0

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    p.join()
    print('主',x)   # 打印子进程的变量x