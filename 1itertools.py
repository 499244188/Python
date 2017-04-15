# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:53:18 2017

@author: Z
"""

import itertools

#因为count()会创建一个无限的迭代器
natuals = itertools.count(1)
for n in natuals:
     print(n)
     

#cycle也会把一个序列无限循环
cs = itertools.cycle('fdsajkl')#字符串也是一种序列
for c in cs:
    print(c)
   
 
    
#repeat把一个元素有限循环
ns = itertools.repeat('abc',3)
for n in ns:
    print(n)

#跳出迭代
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x<22,natuals)
list(ns)


#chain()可以把一组迭代对象串联，形成更大的迭代器
for c in itertools.chain('abc','ABC','ZXC'):
    print(c)
    
#froupby()把迭代器中相邻的元素放在一起
for key,group in itertools.groupby('aaasssfffffkkkaaaa'):
    print(key,len(list(group)))
       
 #froupby()把迭代器中相邻的元素放在一起
for key,group in itertools.groupby('aaaAAssSsfffffkkkaaaa',lambda x: x.upper()):
    print(key,len(list(group))) 
       