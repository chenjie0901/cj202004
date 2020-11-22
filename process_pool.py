from multiprocessing import Pool
import time
import random

def task(task_name):
    print('开始做任务：',task_name)
    strat=time.time()
    time.sleep(random()*2)
    end=time.time()
    print('完成任务用时：'，(end-start)

if __name__=='__main__':
    pool=Pool(5)

    tasks=['听音乐','吃饭','洗衣服','打游戏','散步','做饭','打球']
    for task in tasks:
        pool.apply_async(task,args=(task,))

    print('over......')