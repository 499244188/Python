# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 11:40:17 2017

@author: Z
"""

import base64
#编码
a = base64.b64encode(b'binary\x00string')
#解码
base64.b64decode(a)


#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
#所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

a= base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
a

b = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b
base64.urlsafe_b64decode(b)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
 
import struct
struct.unpack('<ccIIIIIIHH',s)
 
import os
f = open(r'C:\Users\Z\Desktop\ab.bmp','rb')
 

l = f.read(30)
struct.unpack('<ccIIIIIIHH',l)
 
 
import hashlib
 
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
 
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
###################################################################
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    return md5.hexdigest()

def login(user,password):
    try:
        if calc_md5(password)==db1[user]:
            print('登录成功')
        else:
            print('密码错误')
    except KeyError as e:
        print('用户名或密码错误',e)
 
login('bob','888888')

calc_md5(db['bob'])==db1[user]


db = {
'michael':'123456',
'bob':'888888',
'alice':'password'
}

db1={

'michael':'0acf4539a14b3aa27deeb4cbdf6e989f',
'bob':'21218cca77804d2ba1922c33e0151105',
'alice':'6384e2b2184bcbf58eccf10ca7a6563c'

}


md5 = hashlib.md5()
md5.update('alice'.encode('utf-8'))
md5.hexdigest()



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 