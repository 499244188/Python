# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:33:55 2017

@author: Z
"""

import threading

#创建全局threadLoca对象
local_school = threading.local()

def process_student():
    #获取当前关联的student:
    std = local_school.student
    print('Hel,%s(in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student = name
    process_student()
    
t1 = threading.Thread(target=process_thread,args =('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()