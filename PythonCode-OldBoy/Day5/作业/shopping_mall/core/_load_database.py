# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

print('../db/DataBase.json')
# 定义一个_load_database函数，用于从json文件中读取信息，默认加载的数据库是database.json文件
def _load_database(filename='../db/DataBase.json'):
    with open(filename) as f:
        database = json.load(f) # 解码JSON数据，将一个JSON编码的字符串转换回一个Python数据结构
    return database # 返回解码后的数据