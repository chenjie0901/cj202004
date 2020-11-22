import time
def dance():
    for i in range(30):
        print('我正在跳舞！')
        time.sleep(0.05)
        pass

def sing():
    for i in range(30):
        print('我正在唱歌！')
        time.sleep(0.05)
        pass

dance()
time.sleep(1)
sing()