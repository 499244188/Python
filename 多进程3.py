# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:03:49 2017

@author: Z
"""
#进程间通信
from multiprocessing import Process,Queue
import os,time,random

#写数据进程
def write(q):
    print('Process to write:%s' %os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' %value)
        q.put(value)
        time.sleep(random.random())
        
#都数据进程
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
        
if __name__=='__main__':
    #父进程创建Queue,并传给各个子进程
    q=Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read, args=(q,))
    
    #启动子进程pw
    pw.start()
    #启动子进程pr
    pr.start()
    
    #等待pw结束
    pw.join()
    
    #进程进入死循环，无法结束，只能强行停止
    pr.terminate()