print('hello dog')
print("1122333")

#输入
#usersss = input('Enter login name:')
#print(usersss)

#注释，自动生成文档
#def foo():
#    "this is a doc"
#    return True

#运算符
print(8//3)
#>>>2
print(8/ 3)
#>>>2.66666666

#乘方
print(26**32)

print(-2*4+3**3)

#比较
print(2<4,2==4,6.2<=6)

print(pow(3,2))

##格式化字符串
print("%s is numnber %d"%("python",21))

#重定向输出
#import sys
#print("fatal erdsfasror",file=sys.stderr)

#logfile = open('C://Users/ZYC/PycharmProjects/std/test/ssss.txt','a')
#print("fate erro:in",logfile)
#logfile.close()

#运算
n = 2
n=n*4
print(n)
n *= 6
print(n)

#字符串
pystr = 'Python'
iscool = 'is cool'
print(pystr[-3:])
laa = pystr+' ' + iscool
print(laa)
labb = pystr *3
print(labb)
print('-+' * 50)
pystr = '''python
... is ccccc'''
print(pystr)

#列表
aList = [1,2,3,4,5,6]
print(aList)
print(aList[2:-2])
print(aList[:-2])
#貌似可以修改
aList[0] = 20
print(aList[0])

aDict = {'host':'192.168.0.0'} #create dict
aDict['port'] = 80 #add to dict
print(aDict)
print(aDict['host'])

for key in aDict:
    print(aDict[key])



# Python
import random
a = random.random()
a=a*10-5
if a > 0:
    print("x是正数")
else:
    print("x为负数")

cj = random.random()*100
print(cj)

if cj>80:
    print('cj>80')
elif cj>50:
    print('cj > 50')
else:
    print("zhazha")

#循环
count = 0
while count<300:
    print('aaaaa%d'%(count))
    count += 1

for item in ['a','ssss','swww' ,'fdef']:
    print(item)
#格式化输出
who = 'knights'
what = 'Ni'
print('we are thie',who,'who say',what,what,what)
print('We Are This %s who say %s'%(who,(what+'-')*4))

for each in range(3):
    print(each)

for each in [2,3,4,5,6]:
    print(each)

#迭代循环字符串
foo = 'String'
for c in foo:
    print(c)

for i in range(len(foo)):
    print(foo[i],'(%d)'%i)

for i,ch in enumerate(foo):
    print(ch,'-%d-' % i )

#----------x的2次方
squared = [x ** 2 for x in range(4)]
print(squared)
for i in squared:
    print(i)
 
# Python
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
  

# Python
#类
class FooClass(object):
    version = 0.1
    def __init__(self,nm='John Doe'):
        self.name = nm
        print('Created a class instance for',nm)
    def showname(self):
        print('You Name is',self.name)
        print('My name is ',self.__class__.__name__)
    def shwcer(self):
        print(self.version)
    def addMe2Me(self,x):
        return x + x
foo = FooClass()

foo.showname()
print(foo.addMe2Me(45))
fbb = FooClass('Dou_Bi')


import sys
sys.stdout.write('Hello world\n')


a = sys.platform
print(a)

print(sys.version)

obj = 245
#a_b = len(obj)
#print(a_b)
'''
print(dir(obj))#显示对象属性，如果没有提供参数，则显示全局变量的名字
print(help(obj))
print(int(obj))
'''
#open(fn,mode) 以mode（‘r’ = 读， ‘w’ = 写）方式打开一个文件
#input(str)等待用户输入一个字符串。可提供str为输入提示信息
#str(obj)将一个对象装换为字符串
#type(obj) 返回一个对象的类型



