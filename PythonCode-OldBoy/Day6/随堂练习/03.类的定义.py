# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

class Dog1(object):
    print("hello, I am a dog1")

d = Dog1() # 实例化这个类
# 此时的d就是类Dog的实例化对象
# 实例化，其实就是以Dog类为模版，在内存里开辟一块空间，存上数据，赋值成一个变量名

# 执行了之后，结果是直接打印print的内容了：hello, I am a dog
# 这种操作是有问题的，比如下面的代码，我们想给狗起名字是传不进去的

class Dog(object):
    def __init__(self,name,dog_type): # 这个叫构造函数，构造方法，也叫初始化方法
        self.name = name
        self.dog_type = dog_type

    def sayhi(self): # 类的方法，类的功能都写到这里，多个功能就写多个类的方法
        print("hello,I am a dog, my name is", self.name)
d = Dog('aaa',"京巴") # 实例化类，实例化后的对象叫实例
d.sayhi() # 调用对象并输出

# 如果把上面两行注释掉的话，输出的是一个内存地址：<class '__main__.Dog'>
# self其实就是实例本身
