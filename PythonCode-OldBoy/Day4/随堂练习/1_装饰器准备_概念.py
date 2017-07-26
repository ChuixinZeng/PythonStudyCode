# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

'''
装饰器：本质是函数（功能是装饰其他函数），就是为其他函数添加附加功能，比如一个人要打扮带耳环
原则：
    1、不能修改被装饰的函数的源代码
    2、不能修改被装饰的函数的调用方式
    3、装饰器对于被装饰的函数式透明的

实现装饰器需要的知识储备：
    1、函数即“变量”
    2、高阶函数
    3、嵌套函数

高阶函数+嵌套函数 =》 实现装饰器的效果

例子：给下面两个函数增加记录日志的功能，之前学习的方法是使用函数，如果有十个函数，就是调用十次，避免重复写代码
如果程序已经运行了呢？
就意味着要修改程序源代码，业务有宕机风险，所以新增功能不能修改源代码，理论上源代码写好了就不要修改了

def logger():
    print("logging")
def test1():
    pass
    logger()
def test2():
    pass
    logger()
test1()
test2()

'''
import time

# timer是一个装饰器，本质就是一个函数
def timer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return warpper

@timer
# 装饰器不修改被装饰程序的代码
def sample1():
    # 模拟test1运行的时间为3秒
    time.sleep(3)
    print("in the test1")

sample1()