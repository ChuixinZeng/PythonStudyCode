# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# Python中return的三种返回情况
# 返回值数=0；返回none
# 返回值数=1；返回object对象，Python中所有的东西都是对象
# 返回值数>1；返回tuple元组

def test1():
    print('in the test1')

def test2():
    print('in the test2')
    return 0

def test3():
    print('in the test3')
    return 1,'hello',['alex','zengchuixin'],{'name':'alex'}

def test4():
    print('in the test4')
    # 下面可以返回test3函数的内存地址空间，<function test3 at 0x000001A57478E488>
    return test3

x = test1()
y = test2()
z = test3()
a = test4()

print(x)
print(y)
print(z) # 结果保存在一个元组中
print(a)