import socket
# 不同电脑间的通信需要使用到socket
# socket可以在不同的电脑间通信，也可以在同一电脑的不同程序之间通信

# 1.创建socket，并连接
# AF_INET:表示这个socket是用来进行网络连接的
# SOCK_DGRAM：表示连接的时一个 UDP 连接
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2.发送数据
# data:要发送的数据
# adress：发送给谁，参数时一个元组，元组两个元素，ip和端口号
# 端口号：0~65536  0~1024 端口号不要使用
s.sendto('hello'.encode('utf8'),('192.168.192.1',9000))

# 3.关闭socket
s.close()