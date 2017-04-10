# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:19:01 2017

@author: Z
"""
import time,threading
'''
import time,threading
#新线程执行代码
def loop():
    print('thread %s is running...' %threading.current_thread().name)
    n = 0
    while n<5:
        n=n+1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' %threading.current_thread().name)
    

print('thread %s is running...' %threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended,'%threading.current_thread().name)
'''



#假定银行存款

blance = 0
lock = threading.Lock()

def change_it(n):
    #先存款，后取款，因该还是0
    global balance
    balance = balance + n
    print('NN=%s'%threading.current_thread().name)
    #print('ban=..%d'%balance)
    balance = balance - n
    #print('ban....%d'%balance)
'''
def run_thread(n):
    for i in range(10):
        change_it(n)
'''    
blance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(10):
        #先获取锁
        lock.acquire()
        print('+')
        try:
            #修改数据
            change_it(n)
        finally:
            #修改完解锁
            lock.release()
            print('-')


t1 = threading.Thread(target=run_thread,args=(4,))
t2 = threading.Thread(target=run_thread,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)





