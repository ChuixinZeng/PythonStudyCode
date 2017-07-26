# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import time
# 不修改源代码的情况下给sample1新增功能
# 高阶函数+嵌套函数
def timer(func): # timer(test1) func = test1 返回了deco的内存地址
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs) # run sample1
        end_time = time.time()
        print("the func run time is %s" %(end_time-start_time))
    return deco

@timer # 语法糖，想把装饰器给哪个函数，就写在哪个函数的头部，相当于下面的sample1=timer(sample1)
def sample1():
    time.sleep(3)
    print("in the sample1")

@timer
def sample2(name,age):
    time.sleep(3)
    print("name:",name,age)

#sample1=timer(sample1)
sample1() # 执行的是deco，没有改变sample1的调用方式，没有改变sample1的代码
# sample2() # sample2执行会报错，因为sample2有参数，而把sample2传给func之后，上面的函数里面的func并没有参数
sample2("zengchuixin","30") # 这样调用，然后前面的装饰器里面加可选参数*args,**kwargs，这样不管被装饰的函数有没有参数都可以正常运行了