# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

'''
with open('yesterday.md','a+') as f:
    f.write('end action')

# 没有函数的情况下，下面的函数想使用上面的写文件的功能，就需要在每个函数里面写一次，太重复了

def test1():
    print('test1 staring action...')

    with open('yesterday.md','a+') as f:
        f.write('end action')

def test2():
    print('test2 staring action...')

    with open('yesterday.md', 'a+') as f:
        f.write('end action')


def test3():
    print('test3 staring action...')

    with open('yesterday.md', 'a+') as f:
        f.write('end action')

'''
import time
# 优化后的版本
def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format) # 引用上面定义好的时间格式
    with open('a.txt', 'a+') as f:
        f.write('%s end action\n' %time_current)

# 没有函数的情况下，下面的函数想使用上面的写文件的功能，就需要在每个函数里面写一次，太重复了

def test1():
    print('test1 staring action...')

    logger()

def test2():
    print('test2 staring action...')

    logger()

def test3():
    print('test3 staring action...')

    logger()
x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)