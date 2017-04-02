# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:04:20 2017

@author: Z
"""
#内存中变成可存储或传输的过程称之为序列化


import pickle
d = dict(name='Bob',age=20,score=88)
pickle.dumps(d)

'''
pickle.dumps()方法把任意对象序列化成一个bytes，
然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()
直接把对象序列化后写入一个file-like Object
'''
#写入文件
f = open('D:\github\python\dump.txt','wb')
pickle.dump(d,f)
f.close()

#读取
f = open('D:\github\python\dump.txt','rb')
d = pickle.load(f)
f.close()
d


#dumps（）返回一个str.类容是标准json
import json
d=dict(name='BOb',age=20,score=88)
json.dumps(d)

json_str='{"age":20,"score":88,"name":"LiMing"}'
json.loads(json_str)

import json

def student2dict(std):
    return{
            'name':std.name,
            'age':std.age,
            'score':std.score
            }

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        
s=Student('Bob',22,43)
print(json.dumps(s,default=student2dict))
#类转为dict
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str='{"age":20,"score":88,"name":"LiMing"}'
print(json.loads(json_str,object_hook=dict2student))