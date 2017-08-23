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

# 定义一个函数_set_shopping_list，用于设定购物清单
def _set_shopping_list(account,c_name,num):
    database = _load_database._load_database()
    # 使用for循环添加购买的商品的数量
    for i in range(num):
        # 将购买的商品添加到字典shopping_list键所对应的列表中
        database[account]['shopping_list'].append(c_name)
        # 将购买信息通过调用_save_account函数保存到json文件中
        _save_account._save_account(database)
