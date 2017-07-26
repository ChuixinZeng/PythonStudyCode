# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 高阶函数的两个特性

import time

#   1.把一个函数名当做实参传递给另外一个函数（实现不修改被装饰函数源代码情况下为其添加功能）
#   这个例子和装饰器的区别是：源代码调用方式被改掉了
def bar():
    time.sleep(3)
    print("in the bar")
def sample(func):
    start_time=time.time()
    func() # 返回具体的bar的值，下面使用了smaple(bar)，相当于bar=func了
    stop_time=time.time()
    print("the func run time is %s" %(stop_time-start_time))

sample(bar) # 返回的是bar的内存地址，相当于房间号

#   2.返回值中包含函数名（好处是可以不修改函数的调用方式）

def bar2():
    time.sleep(3)
    print("in the bar2")
def sample2(func):
    print(func) # 返回内存地址
    return func
# print(sample2(bar2)) # 返回内存地址
#sample2(bar2()) # 这个地方bar2加上小括号，等于把返回值传给func了，就不符合高阶函数的定义了，只传函数名
bar2 = sample2(bar2) # 可以理解为为bar2添加了新功能，来自sample2
bar2() # 运行bar2函数，调用方式没有改变