# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 参数组就是指非固定函数
# 前面的定义的函数有个问题，就是调用的参数超过了定义的形参，就会报错
# 用于实参数目不固定的情况下，如何去定义形参
# *后面跟的是变量名，不一定写args，但是规范就是args，统一写args比较好
# *args：接受N个位置参数，不是关键字参数，转换成元组的形式
# *kwargs，接收N个关键字参数，转换成元组的形式
def test(*args):
    print(args)

# 打印的结果是一个元组，多个实参被放到了一个元组里面
test(1,2,3,4,5)
# 还可以按照下面的进行传递，相当于*args = *[1,2,3,4,5]
test(*[1,2,3,4,5])

# 和位置参数结合起来
# 参数组的扩展性比较强，后期需要扩展的时候，比较方便

def test1(z,*zeng):
    print(z)
    print(zeng)
test1(1,2,3,4,5,6,7)

'''
# **kwargs把n个关键字参数转换成字典的方式
def test2(**kwargs):
    print(kwargs)
    # 取字典中的值
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

# 关键字参数，把关键字参数传递给kwargs，kwargs把实参当作字典格式进行处理
test2(name='alex',age='22',sex='f')
# 也可以写成
test2(**{'name':'alex','age':8,'sex':'f'})
'''
'''
# 和位置参数结合
def test3(name,**kwargs):
    print(name)
    print(kwargs)
test3('alex',age=18,sex='m')
'''
'''
# 和位置，关键字参数混用
def test4(name,age=8,**kwargs):
    print(name)
    print(age)
    print(kwargs)

test4('alex',sex='m',hobby='tesla')
# 给默认参数赋值可以以位置参数的形式赋值
test4('alex',3,sex='m',hobby='tesla')
# 也可以按照下面的方式把默认参数写到后面
test4('alex',sex='m',hobby='tesla',age=3)
'''
# 所有的参数类型一起混用
def test4(name,age=8,*args,**kwargs):
    print(name)
    print(age)
    print(kwargs)
# 下面的*args只能接收位置参数不能接收关键字参数，所以*args下面的值是空值
test4('alex',age=3,sex='m',hobby='tesla')