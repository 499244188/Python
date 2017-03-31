#文件的操作
#handle = open(file_name,access_modde = 'r')
'''
filename = input("Enter File name:")
fobj = open('a.txt','r')
for eachLine in fobj:
    print(eachLine)
fobj.close()
'''
#错误和异常
'''
try:
    file = input("Enter file")
    fobj = open(file,'r')hjk
    for eachLine in fobj:
        print(eachLine),
    fobj.close()
except IOError,e:
    print('file open erro:',e)
'''
def addME2ME(x):
    return(x + x)

print(addME2ME(34))

print(addME2ME([1,'fdas',45]))

def foo(debug = True):
    if debug:
        print('in debug mode'),
    print('done')

foo()
print('-='*20)

foo(True)
print('-='*20)
foo(False)

'''
class ClassName(base_class[es]):
    '''







