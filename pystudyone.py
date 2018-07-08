#coding=utf-8
#python学习记录 2018-07-08
print '你好'
a=1
b=2
c=a+b
if b>9:
    print str(b)+'大于9'
elif b==9:
    print str(b)+'等于9'
else:
    print str(b)+'小于9'


while b<9:
    print b
    b=b+1
    if b==6:
        continue
    if b==7:
        break
    else:
        print b
for letter in 'python':
        print letter
for i in ['a','b','c','d']:
    print i
array=['a','b','c','d']
for i in range(len(array)):
    print array[i]



for num in range(10,100):
    for i in range(2,num/2):
        if num%i==0:
            break;
    else:
        print str(num)+"是一个质数"

#数字类型不允许改变
num=5
num2=2
print num
print num2
del num,num2
longnum=1234567890L
floatnum=2.3234e-2
convertint=int('434')
print convertint
convertint=int(1.6)
print convertint
import cmath
import math
print cmath.sqrt(9)
print math.ceil(4.5)#四舍五入
print math.exp(1)#e^x
print math.log(100,10)
print math.modf(10.90)
print math.pow(2,4)#2^4
#随机数
import random
print random.choice([1,2,3,4,5,6,7])
print random.randint(1,100)
print random.randrange(10,100)
print random.random()
lst=[]
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
print random.uniform(2,10)
varstr='hi its me'
print varstr[:2]+'its kio'
print '%s%d'%('me',90)
triplestr=''' cloud
google'''
print triplestr

