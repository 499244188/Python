#！/usr/bin/env/ python

import types
def displayNunTypeB(num):
    print(num,'is')
    if isinstance(num,(int,float,complex)):
        print('a number of type:',type(num).__name__)
    else:
        print('not a number at all')


def displayNunType(num):
    print(num,'Is')
    if type(num) == type(0):
        print('An Integer')
    elif type(num) == type(0.0):
        print('A Float')
    elif type(num) == type(0+0j):
        print('A Complex')
    else:
        print('not a number at all')



displayNunType(22)
displayNunType(23+4j)
displayNunType("jkljl")
displayNunType(-232)
displayNunType('2323')
displayNunType(0)
displayNunType(None)