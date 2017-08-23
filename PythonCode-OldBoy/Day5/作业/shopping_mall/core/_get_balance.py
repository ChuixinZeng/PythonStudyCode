# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

from core import _load_database

# 定义一个函数_get_balance，用于获取账户余额
def _get_balance(account):
    database = _load_database._load_database()
    # 将字典中账户的余额信息读取到account_balance变量
    account_balance = database[account]['balance']
    # 返回账户余额变量的值
    return account_balance