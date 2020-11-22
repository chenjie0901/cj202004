import socket

# 创建一个基于TCP的socket连接
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.43.218',9090))

s.listen(128)       # 把socket变成一个被动监听的socket
# m=s.accept()      # 接收客户端的请求,接收到的为一个元组，
# 第0个为客户端的socket连接
# 第1个为客户端的ip和端口号
client_socket,client_addr=s.accept()
data=client_socket.recv(1024)      # 每次读取服务端网卡收到的1024个字节内容

print('接收到了{}客户端{}端口号发送的数据内容是：{}'.format(client_addr[0],client_addr[1],data.decode('utf8')))

# s.close()