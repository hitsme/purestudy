#!/usr/bin/python
#-*- coding: utf-8 -*-
class Employee:
    '员工类'
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayEmpCount(self):
        print 'Total Employee %d'%Employee.empCount
    def displayEmployee(self):
        print 'name:%s,salary:%d'%(self.name,self.salary)
ep=Employee('mgl',9000)
ep.displayEmpCount()
ep.displayEmployee()
ep.salary=10000
print ep.displayEmployee()
print hasattr(ep,'name')
print getattr(ep,'name')
setattr(ep,'salary',15000)
print getattr(ep,'salary')
#delattr(ep,'salary')

print 'Employee.__doc__:',Employee.__doc__
print 'Employee.__name__:',Employee.__name__
print 'Employee.__module__',Employee.__module__
print 'Employee.__bases__',Employee.__bases__
print 'Employee.__dict__',Employee.__dict__

#python对象销毁（垃圾回收） 1.引用计数器 2.循环垃圾收集器
#python使用引用计数这一简单技术来跟踪和回收垃圾
#在python内部记录所有使用中的对象各有多少引用
#一个内部跟踪变量，称为引用计数器
#对象创建，创建一个引用计数，引用计数为0时，由解释器在适当的时机将垃圾对象进行回收占用的内存空间

#析构函数__del__,在对象销毁的时候被调用，对象不再被使用调用
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print class_name,"销毁"
p=Point(12,10)
p1=p
p2=p1
del p2
del p
del p1

#类的继承 面向对象编程好处之一就是代码重用，而代码重用可以通过类继承机制
#继承语法 class 派生类(基类)

class Parent:
    parentAttr=100
    def __int__(self):
        print '调用父类构造函数'
    def parentMethod(self):
        print '调用父类方法'
    def setAttr(self,attr):
        Parent.parentAttr=attr
    def getAttr(self):
        print '父类属性：',Parent.parentAttr
class Child(Parent):
    def __int__(self):
        print '调用子类构造方法'
    def childMethod(self):
        print '调用子类方法'
c=Child()
d=Parent()
c.childMethod()
c.parentMethod()
c.setAttr(1000)
c.getAttr()

#继承多个类 class A(B,C)
print issubclass(Child,Parent)#A是否B的子类
print isinstance(c,Child)

#基础重载方法
#构造函数 __init__(self)
#析构方法 __del__(self)
#转化为供解释器读取的形式 __repr__(self)
#将对象转化成适合string __str__(self)
#对象 比较调用方法cmp(obj,x)  __cmp__(self)

#运算符重载

class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'Vectot(%d,%d)'%(self.a,self.b)
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)
v1=Vector(1,2)
v2=Vector(3,4)
print v1+v2

#类的属性与方法
#私有属性
#__private_attrs 两个下划线开头，声明该属性为私有
#__private_method 两个下划线开头表示该方法为私有方法 内部调用self.__private_method
class JustCounter:
    __secretCount=0#私有变量
    publicCount=0
    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print self.__secretCount
counter=JustCounter()
counter.publicCount
#python不允许实例化的类访问私有数据，可以使用object._classname__attrname
print counter._JustCounter__secretCount
#单下划线 双下划线 头尾双下划线说明
#__func__ 定义特殊方法 一般是系统定义名字 类似__init__
#_foo 以单下划线开头表示protected类型变量或者函数 只能子类及自身访问
#__foo 双下划线表示私有类型private的变量 只能类的内部使用

