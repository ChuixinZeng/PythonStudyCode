# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 有参数的函数

def test(x,y):
    print(x)
    print(y)

# 函数执行时，后面要传递实际的参数
# 下面的1,2是实际存在的参数，叫实参，占用地址空间的
# 上面函数里面定义的xy是形参
# 如果不调用x,y，那么x,y就不存在，不占地址空间

#  位置参数调用，实参和形参必须是一一对应的关系，个数不能超
test(1, 2)

# 下面的是关键字参数调用，y和x不需要与形参一一对应，与形参顺序无关
test(y=1,x=2)
a = 2
b = 1
test(y=a, x=b)

# 如果既有关键字调用，又有位置参数调用，那么会按照位置参数的来
test(3,y=2)
# test(3,x=2)会运行失败

# 关键参数不能写在位置参数前面

def test1(a,b,c):
    print(a)
    print(b)
    print(c)

test1(3, c=2, b=6)