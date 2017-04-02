# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:44:36 2017

@author: Z
"""
"""仅在BSD内核使用（Mac,linux）
import os
print('Rrocess(%s) start...'% os.getpid())

pid = os.fork()

if pid = 0:
    print('I am child process （%s) and my parent is %s.' %(os.getpid(),os.getppid())
else:
    print('I (%s) just created a child process(%s).'%(os.getpid(),pid))
    
"""

from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))
    
if __name__=='__main__':
    print('Parent process %s.' %os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')
    

