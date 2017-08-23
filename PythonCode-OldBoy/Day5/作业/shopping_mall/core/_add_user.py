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
#
def _add_user():
    # 首先调用_load_database函数，将json文件解码出来，放到database变量
    database = _load_database._load_database('../db/DataBase.json')
    # 执行while循环
    while True:
        # 提供交互式界面，让用户输入要创建的用户名称
        username = input('请输入您的账户名称：').strip()
        # 判断是否存在重名的用户，如果有，则告诉用户，继续执行while循环，让用户输入
        if username in database:
            print('用户名已经存在，不需要重复创建！')
        # 如果没有，则用户输入信息有效，中断while循环
        else:
            break
    # 执行while循环
    while True:
        # 让用户输入两次密码
        pwd1 = input('请输入您的账户密码：').strip()
        pwd2 = input('请再次输入您的账户密码：').strip()
        # 对两次输入的密码信息进行比对
        # 如果面膜不正确，则继续执行while循环让用户重新输入
        if pwd1 != pwd2:
            print('2次输入的密码不通，请重新输入')
        # 如果输入的密码是正确的，则告诉用户创建账户成功
        else:
            print('创建用户成功，开始购物吧！')
            # 把用户创建的账户和密码信息保存到database字典中
            # username为用户账号,pwd1为用户密码,balance为账户余额,shopping_list为购物清单,shopping_time为购物时间
            database[username] = {'pwd':pwd1,'balance':0,'shopping_list':[],'shopping_time':None}
            # 调用_save_account函数，将创建好的账户信息和账户的初始余额、初始购物时间信息保存到json文件
            _save_account._save_account(database)
            # 退出while循环
            break