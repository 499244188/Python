from string import Template
import re
s = Template('There are ${ho} ${la} There are 3 Python Quotation')
print(s.substitute(la ='Python',ho = 3))
#print(s.substitute(la ='Python'))#报错
print(s.safe_substitute(la = 'C++'))

#原始字符串
print('END')
print('\n')
print('Fast')

'''
d = open('E:\X\python\a1.txt')
f = open('E://X/python/a1.txt','r')
for li in f:
    print(li)
'''
'''
m = re.search(r'\\[rtfvn]',r"Hello World\n")
if m is not None:
    m.group()
print('abc')
print(u'abc')
print(u'\u1234')
'''
str1 = 'abc'
str2 = 'xyz'
print(cmp())




















