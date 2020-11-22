from multiprocessing import Process
import time
import os

def task(n):
    print('子进程的PID：%s' %os.getpid())

if __name__ == '__main__':
    p=Process(target=task,args=(3,),name='子进程')    # 修改进程的名称为"子进程"
    p.start()
    print(p.is_alive())
    p.terminate()            # 给操作体统发送指令，把进程释放掉
    time.sleep(1)            # 应用程序不能直接终止掉进程，需要等待操作系统终止进程
    print(p.is_alive())      # 判断进程是否处于一个活动状态
    print('主')