# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:07:09 2017

@author: Z
"""

import socket

#创建一个socker:
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
ss.connect(('www.sina.com',80))
#发送数据
ss.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')



#接收数据
buffer = []
while True:
    #每次最多接受多少字节
    d = ss.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#也可以recv(max),知道数据空

#关闭连接
ss.close()


header,html = data.split(b'\r\n\r\n',1)

print(header.decode('utf-8'))
#把接受的数据写入文件：
with open('e:\\sina.html','wb') as f:
    f.write(html)
    
f.close()

###################################################
#服务端
import socket
fs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口
fs.bind(('127.0.0.1',9999))
fs.listen(5)
print('Waiting for connection...')

import threading

while True:
    #接受一个连接
    sock,addr = fs.accept()
    #创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



import time
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'% addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello ,%s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.'%addr)
######################################################
#客户端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))
#接受消息
print(s.recv(1024).decode('utf-8'))
for data  in [b'Michael',b'Tracy',b'Sarah']:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()