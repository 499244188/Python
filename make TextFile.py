#！/usr/bin/env/ python

'makeTextFile.py --create text file'

import os
ls = os.linesep

#get filename


path1 = 'E://X/python/123.txt'
while True:
    if os.path.exists(path1):
        print('ERROR:%s already exists'%path1)
    else:
        break

#get file content(text) lines
all = []
print('\nEnter lines(.by itself to quit).\n')

#loop until user terminates input
while True:
    entry = input('>')
    if entry =='.':
        break
    else:
        all.append(entry)

#write lines to fuile with proper line-ending
fobj = open(path1,'w')
fobj.writelines(['%s%s'%(x,ls) for x in all])
fobj.close()
print('Done!')
