# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

from core import  _load_database
from core import _save_account

# 定义一个函数_set_shopping_time,设置并记录购物的时间，函数里面定义了一个参数account，用于保存账户信息
def _set_shopping_time(account):
    database = _load_database._load_database() # 设定要记录到哪个数据库，这里使用的是前面定义好的函数_load_database定义的database.json
    d1 = datetime.datetime.now() # 设置购物时间为当前时间
    d2 = d1.strftime('%Y-%m-%d %H:%M:%S') # 将当前时间进行格式转换
    database[account]['shopping_time'] = d2 # 将转换好的时间记录到字典里面的shopping_time键上
    _save_account._save_account(database) # 保存购物时间到数据库中，这里的数据库是指database.json文件