# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import time
# 不修改源代码的情况下给sample1新增功能
# 高阶函数+嵌套函数

def timer(func): # timer(sample1) func = sample1 返回了deco的内存地址
    def deco():
        start_time = time.time()
        func() # run sample1
        end_time = time.time()
        print("the func run time is %s" %(end_time-start_time))
    return deco

@timer # 语法糖，想把装饰器给哪个函数，就写在哪个函数的头部，相当于下面的sample1=timer(sample1)
def sample1():
    time.sleep(3)
    print("in the sample1")

@timer
def sample2():
    time.sleep(3)
    print("in the sample2")

#sample1=timer(sample1)
sample1() # 执行的是deco，没有改变sample1的调用方式，没有改变sample1的代码
sample2()