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

