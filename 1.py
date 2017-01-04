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
