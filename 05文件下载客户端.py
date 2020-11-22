import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.31.199',9090))

file_name=input('请输入您要下载的文件名：')

s.send(file_name.encode('utf8'))
content=s.recv(1024)
with open(file_name,'wb') as file:
    file.write(content)

s.close()