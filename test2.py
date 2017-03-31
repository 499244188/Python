import math

'''
for i in range(1,10):
    print(round(2.5,i))
'''

for i in range(10):
    print(round(math.pi,i))
'''
  函数                           功能
abs(num) 返回 num 的绝对值
coerce(num1, num2) 将num1和num2转换为同一类型，然后以一个 元组的形式
返回。
divmod(num1, num2) 除法－取余运算的结合。返回一个元组(num1/num2,num1 %
num2)。对浮点数和复数的商进行下舍入（复数仅取实    
数部分的商）
pow(num1, num2, mod=1) 取 num1 的 num2次方，如果提供 mod参数，则计算结果
再对mod进行取余运算
round(flt, ndig=0) 接受一个浮点数 flt 并对其四舍五入，保存 ndig位小数。
若不提供ndig 参数，则默认小数点后0位。
round()仅用于浮点数。（译者注：整数也可以， 不过并没有什么
实际意义）
'''