# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 函数嵌套：在一个函数体内用def去声明一个函数，而不是去调用另外一个函数（直接输函数名是调用函数）
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()

# bar()在函数外面无法调用bar()类似于局部变量的概念,所以这个函数有局部变量的特性
# 作用域是从里面往外找，所以下面代码的值是3
# 通过加断点可以发现执行时从外面往里面执行
x=0
def grandpa():
    x=1
    def dad():
        x=2
        def son():
            x=3
            print(x)
        son()
    dad()
grandpa()