import socket
# 创建一个基于 udp 的网络socket连接
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定端口号和IP地址
s.bind(('192.168.43.117',9090))

# recvfrom 接受数据

content=s.recvfrom(1024) #阻塞等待
print(content)
# 接收到的数据是一个元组，元组里有两个元素
# 第0个是接收到的数据，第1个是发送方的IP地址
# print('从{}地址{}端口号接收到了消息，内容是{}'.format(addr[0],addr[1],data.decode('utf8')))

s.close()