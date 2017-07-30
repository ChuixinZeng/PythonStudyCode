# -*- coding:utf-8 -*-
# Author:Chuixin Zeng

# 程序的执行文件在bin下面
# 必须让环境变量知道父目录的存在，加相对路径
# 返回当前程序的相对路径（在pycharm里面显示的是绝对路径，实际上是相对路径）
print(__file__)

# 必须获取到程序的绝对路径，动态的加入到系统环境变量中
import os
import sys
# print(os.path.abspath(__file__))
#
# # 上面找到当前程序的绝对路径了，现在取上一级的绝对路径
# # dirname是指去掉当前路径中的文件名，到bin目录
# print(os.path.dirname(os.path.abspath(__file__)))
# # 去掉文件名之后，再往上找一级，到ATM目录
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# 现在可以导入conf、core程序包了，下面标红不是出错，是pycharm的问题
import conf,core
from conf import settings
from core import main

# 调用main里面的login函数了
main.login()
