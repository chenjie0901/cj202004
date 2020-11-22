import socket,os

sever_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sever_socket.bind(('192.168.43.117',9090))
sever_socket.listen(128)

client_socket,client_addr=sever_socket.accept()
file_name=client_socket.recv(1024)

print('接收到了来自{}地址{}端口的数据，内容是：{}'.format(client_addr[0],client_addr[1],file_name.decode('utf8')))
if os.path.isfile(file_name.decode('utf8')):
    # print('读取文件返回客户端')
    with open(file_name,'rb') as file:
        # print(file.read())
        content=file.read()
        client_socket.send(content)
else:
    print('文件不存在')
