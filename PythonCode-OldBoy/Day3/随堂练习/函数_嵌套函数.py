# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 下面是错误的例子，程序执行时，函数还没有定义
'''
def test4(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")
test4('alex',age=34,sex='m',hobby='tesla')
def logger(source):
    print("from %s" % source)
'''
# 下面是正确的例子，先执行函数的定义，然后最后一行test4回过头去找test4函数执行，函数里面又嵌套了logger函数
def test4(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")

def logger(source):
    print("from %s" % source)

test4('alex',age=34,sex='m',hobby='tesla')
