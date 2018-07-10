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
pass#nothing to do





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
print triplestr*2+'1'
print 'bingo'.capitalize()
print 'bingo   hero'.center(200)
print 'bingogogo'.count('go')
print 'hangzhou is begin'.decode(encoding='UTF-8',errors='strict')
print 'hangzhou'.endswith('zhou')
print 'hangzhou'.join(['1','2','3'])
print 'hi   '.lstrip()
print max('abcd')
print min('abcd')
print 'abcD'.swapcase()
print 'hello you'.title()

list=['a','b','c','d']
del list[0]
print list[0]

dict={'name':'l','age':25,'adress':'hn'}
print dict['name']
#修改字典
dict['name']='m'
print dict['name']
del dict['name']
dict.clear()
#日期时间
import time;
ticks=time.time()
print ticks
print time.localtime(ticks)
print time.asctime(time.localtime(ticks))
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

import calendar
print calendar.month(2018,7)
print time.clock()
time.sleep(5)
#python函数
def printmethod(str):
    print str
    return
printmethod("hi function".title())

def changeme( mylst):
    mylst.append([1,2,3,4,5])
    print mylst
    return
mylst=[10,20,30]
changeme(mylst)
print mylst

changeme(mylst=[10,20,30])

def person(name,sex='man'):
    print name+','+sex
    return
person(name='liang')
person('liang')
#不定长参数
def personmore(arg1,*vartuple):
    print arg1
    for i in vartuple:
        print i
    return
personmore('a','b','c','d')
#python 使用lambda
sum=lambda arg1,arg2:arg1+arg2;
print sum(1,2)

#python 模块 一个python文件就是一个模块
#导入模块，python解析器，首先对模块位置的搜索顺序是：
#当前目录 如不在则搜索在shell变量pythonpath下的每个目录
#如果找不到，python查看默认路径，unix，默认路径一般为/usr/local/lib/python

#全局变量
m=1000;
def globalparam():
    global m
    m=m+1
    return
globalparam()
print m

def tglobals():
    print globals()
    print locals()
tglobals()
reload(random)

from model1.model1 import testmodel1
testmodel1()

#python文件I/O
#读取键盘输入 raw_input("")
inputstr=raw_input("输入：")
print inputstr
#input函数
str=input("输入")
print str

#打开和关闭文件
#open函数 file object =open(filename,accessmode,buffering)
opfile=open('test.txt','w+')
print opfile.name
print opfile.closed
print opfile.mode
opfile.writelines("hello")
print opfile.readlines()[0]
opfile.close()

opf=open('test.txt','w+')
str=opf.read(10)
print str
print opf.tell()
print opf.read(10)
opf.seek(0,0)
str2=opf.read(10)
print str2
opf.close()
#重命名删除文件
import os
#os.rename('test.txt','hello.txt')
#os.remove('hello.txt')
#os.mkdir("mkdir")
#os.chdir("dir")改变当前目录

#获取当前工作目录
print os.getcwd()
#删除目录
#os.rmdir("/tmp/test")


#异常处理 syntaxError语法错误 indentationError缩进错误
try:
    fo=open("tesy.txt")
    fo.write("测试一下")
except IOError:
    print "Error :没有找到文件，或者读取文件失败！"
else:
    print "内容写入文件成功！"
    fo.close()

try:
    fh=open('testfile.txt','w')
finally:
    fh.close()

def temp_convert(var):
     try:
         return int(var)
     except ValueError,Argument:
         print '参数没有包含数字\n',Argument
temp_convert("xyz")

#可以使用raise来触发异常
def raisefunc(level):
    if level>1:
        raise Exception('Invalid level!',level)
try:
  raisefunc(2)
except Exception:
    print '异常'

#自定义异常
class Networkerror(RuntimeError):
    def __int__(self,arg):
        self.args=arg
try:
    raise Networkerror("bad hostname")
except Networkerror,e:
    print e.args

