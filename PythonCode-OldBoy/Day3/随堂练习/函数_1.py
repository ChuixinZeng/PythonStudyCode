# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 面向对象——》类——》class
# 面向过程——》过程——》def
# 函数式编程——》函数——》def


# 定义一个函数
def funcl():
    ''' testing1 ''' # 函数说明
    print('in the funcl') # 代码块定义
    return 0  # 返回值

# 定义一个过程
def func2():
    ''' testing2 '''
    print('in the func2')

# 调用函数和过程
# 函数和过程都可以调用
# 过程实际上就是没有返回值的函数而已

x = func2()
y = funcl()

# 但在Python中过程也被当做函数，下面过程的返回值是none
print('form func1 return is %s' %x)
print('from func2 return is %s' %y)