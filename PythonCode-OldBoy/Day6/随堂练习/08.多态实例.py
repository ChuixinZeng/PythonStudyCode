# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

'''

多态性（polymorphisn）是允许你将父对象设置成为和一个或更多的他的子对象相等的技术，赋值之后，
父对象就可以根据当前赋值给它的子对象的特性以不同的方式运作。简单的说，就是一句话：允许将子类类型的指针赋值给父类类型的指针。
那么，多态的作用是什么呢？我们知道，封装可以隐藏实现细节，使得代码模块化；继承可以扩展已存在的代码模块（类）；
它们的目的都是为了——代码重用。而多态则是为了实现另一个目的——接口重用！多态的作用，就是为了类在继承和派生的时候，
保证使用“家谱”中任一类的实例的某一属性时的正确调用。

Pyhon 很多语法都是支持多态的，比如 len(),sorted(), 你给len传字符串就返回字符串的长度，传列表就返回列表长度。

'''

# 如果是做自动化的，实际情况下用类就够了，很难用到多态和继承。

class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method") # 定义一个接口，子类必须先重构它，否则抛出错误


class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


def func(obj):  # 一个接口，多种形态
    obj.talk()


c1 = Cat('小晴')
d1 = Dog('李磊')

func(c1)
func(d1)