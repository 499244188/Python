
#！usr/bin/env/ python
'''
注释
'''
CODEC = 'utf-8'
FILE = 'unicode.txt'
'''
hello_out = u"Hello woekd\n"
byt_out = hello_out.encode(CODEC)
f = open(FILE,'w')
f.write(byt_out)
f.close()

f = open(FILE,'r')
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print(hello_in)
'''

'''
模块 描述
string 字符串操作相关函数和工具，比如 Template 类.
re 正则表达式:强大的字符串模式匹配模块
struct 字符串和二进制之间的转换
c/StringIO 字符串缓冲对象，操作方法类似于 file 对象.
base64 Base 16,32,64 数据编解码
codecs 解码器注册和基类
crypt 进行单方面加密
diffliba
 找出序列间的不同
 hashlibb
 多种不同安全哈希算法和信息摘要算法的 API
hmac
 HMAC 信息鉴权算法的 Python 实现
md5d
 RSA 的 MD5 信息摘要鉴权
rotor 提供多平台的加解密服务
shad
 NIAT 的安全哈希算法 SHA
stringprepe
 提供用于 IP 协议的 Unicode 字符串
textwrape
 文本打包和填充
unicodedata Unicode 数据库

'''

alist = [123,'abc',4.56,['inner','list'],7-9j]
print(alist)

alist.append('add')
print(alist)
alist.remove(4.56)
print(alist)
del alist[2]
print(alist)
alist = range(1,10)
print(alist)
for i in  enumerate(alist):
    print(i)

a = [2,4,5,8,9,54,2,1]
a.sort()
print(a)
a.reverse()
print(a)