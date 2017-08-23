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
# 定义一个函数_set_balance，用于计算购买商品后，所剩下的余额
def _set_balance(account,num):
    database = _load_database._load_database()
    # 购买商品后，扣除购买的商品的价格
    database[account]['balance'] -= num
    # 将余额信息通过调用_save_account函数保存到json文件中
    _save_account._save_account(database)
