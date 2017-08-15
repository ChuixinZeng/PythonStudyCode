# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# import module_test
# # 下面的调用模块的方式是可以简化的，是在重复的找module_test模块
# def logger():
#     module_test.test # 调用module_test模块里面的函数
#     print("in the logger")
# logger()
#
# def search():
#     module_test.test()
#     print("in the search")
# search()

# 下面是简化的版本
from module_test import test
def logger():
    test() # 调用module_test模块里面的函数
    print("in the logger")
logger()

def search():
    test()
    print("in the search")
search()