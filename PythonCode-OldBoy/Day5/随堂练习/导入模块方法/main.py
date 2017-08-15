# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 第一种导入模块方式，导入的是Module_alex，所以调用的时候要用module_alex.的形式
# import module_alex
# print(module_alex.name)
# module_alex.say_hello()

# 第二种导入模块的方式，导入的不是module_alex，而是module_alex里面的代码，所以调用的使用直接使用module_alex里面的方法就行
# from module_alex import *
# logger()

# 如果此时在main.py里面又定义了一个Logger函数，这个时候执行的时候，logger函数会覆盖导入的模块里面的logger的内存地址
# 所以执行的时候main.py里面新定义的logger函数生效

# 为了避免导入的模块和现有的py里面的函数名称冲突，可以使用下面的写法
from module_alex import logger as logger_alex
logger_alex()

def logger():
    print('in the main')
logger()

# 导入包的本质就是去解释包下面的init.py文件
import Package_test