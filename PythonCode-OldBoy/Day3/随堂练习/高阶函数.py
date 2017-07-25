# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 普通函数

def add(a,b):
    return  a+b

# 高阶函数
# abs代表绝对值
def add(a,b,f):
    return f(a)+f(b)
res = add(3,-6,abs)
print(res)