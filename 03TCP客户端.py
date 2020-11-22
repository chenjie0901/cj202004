import socket

# 基于TCP协议的socket连接
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 在发送数据时，必须要先和服务器建立连接
s.connect(('192.168.43.218',9090))
s.send('hello'.encode('utf8'))

# udp直接使用sendto发送数据
# s.sendto('hello'.encode('utf8'),('192.168.31.199',9090))

s.close()