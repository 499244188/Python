r = open('D:\github\Python\文件读写测试.txt', 'r')
for line in r.readlines():
    print(line.strip())
#print(r.read())
#r.read()
r.close()
#如果文件不存在，就这样写
#try:
#    r = open('D:\github\Python\文件读写测试1.txt', 'r')
#    print(r.read())
#finally:
#    if r:
#        r.close()
#简单的写法
#with open('D:\github\Python\文件读写测试.txt','r') as f:
 #   print(f.read())

f = open('D:\github\Python\文件读写测试.jpg', 'rb')
f.read()

#errors = 'ignore 遇见非法字符编码忽略
f = open('D:\github\Python\文件读写测试.txt', 'r',encoding='utf-8',errors='ignore')
f.read()

#写文件
f = open('D:\github\Python\文件读写测试.txt', 'w')
f.write('Hello, world!!')
f.close()

with open('D:\github\Python\文件读写测试.txt', 'w') as f:
    f.write('HHHHHHHHHH')
    
from io import StringIO
f = StringIO()
f.write('Hello')
f.write('')
f.write('world')

#getvalue()方法用于获得写入后的str。
print(f.getvalue())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

import os
os.name
#os.uname()  win系统不提供
os.environ   #获取环境变量
os.environ.get('PATH')

#查看当前目录的绝对路径
os.path.abspath('.')
#合并路径
os.path.join('D:\github\Python','测试目录')
#创建目录
os.mkdir(os.path.join('D:\github\Python','测试目录'))
os.rmdir('D:\github\Python\测试目录')

#两个路径合成一个时使用，os.path.join()
#路径拆分时，os.path.split()
#拆分路径
os.path.split('/path/to/file.txt')
#重命名文件
os.rename('D:\github\Python\文件读写测试.txt','rn测试文件.txt')
os.remove('D:\github\python\文件读写测试1.txt')

#列出文件下所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
#列出文件下所有文件
[x for x in os.listdir('.') if os.path.isfile(x)]
#列出文件下指定类型文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#返回文件大小。日期。名称。
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
