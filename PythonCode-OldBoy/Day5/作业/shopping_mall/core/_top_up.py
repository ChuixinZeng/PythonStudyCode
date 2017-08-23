# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os
from core import _load_database
from core import _save_account
from core import _get_balance

# 定义一个函数，用于执行充值操作
def _top_up(account):
    database = _load_database._load_database()
    # 进入循环
    while True:
        # 提供交互式界面让用户输入要充值的金额
        num = input('请输入您要充值的金额:')
        # 判断如果用户输入的是不是纯数字，则将充值后的金额更新到数据库
        if num.isdigit():  # 判断输入是否为纯数字(充值的数据必须为纯数字)
            database[account]["balance"] += int(num)  # 将str格式的"纯数字"转换为int格式
            _save_account._save_account(database)  # 保存到文件
            account_balance = _get_balance._get_balance(account)  # 再从文件中读取余额信息
            # 高亮打印充值后的余额信息
            print('您已成功充值,您的余额为\033[32m%d\033[0m元' % account_balance)
            # 上面已经打印余额了，所以这里定义一个return none代表不使用return的方式返回余额
            return None

        # 如果用户输入的不是纯数字，则提示输入错误，重新进行while循环，让用户重新输入
        else:
            print('您的输入有误,请重新输入!')