# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

from core import _load_database

# 定义一个函数，用于获取已经保存过的购物时间
def _get_datetime(account):
    database = _load_database._load_database()
    data = database[account]['shopping_time']
    # 返回变量data的值，变量data保存的就是account键对应的购物时间值，这个值是从json里面解码出来后到字典里
    # 由json到Python可识别的字典数据的解码过程由_load_database函数完成
    return data