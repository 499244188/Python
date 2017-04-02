# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 17:51:27 2017

@author: Z
"""

import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:',p.returncode)

