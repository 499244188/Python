# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:27:08 2017

@author: Z
"""
#服务端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
while True:
    #接受数据
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s.'% addr)
    s.sendto(b'Hello,%s!'% data,addr)
    
#客户端：
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarch']:
    #发送数据
    s.sendto(data,('127.0.0.1',9999))
    #接受数据
    print(s.recv(1024).decode('utf-8'))    
s.close()