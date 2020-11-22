from multiprocessing import Process
import time

def task(name):
    print("%s start" % name)
    time.sleep(3)
    print("%s stop" % name)

if __name__ == '__main__':
    p = Process(target=task,args=("jerry",))
    p.start()
    print("我是主进程!!!")
    time.sleep(10)
    print("我是主进程!!! over")







 