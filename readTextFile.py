#!/usr/bin/env Python

'readTextFile.py --read and display text file'

#get filename
fname = input("Enter filename:")
print()

#attempt to open file for reading

try:
    fname = 'E://X/python/'+fname
    fobj = open(fname,'r')
except IOError as e:
    print('*** file open error:',e)
else:
    #display contents to the screen
    for eachLine in fobj:
        print(eachLine)
    fobj.close()
