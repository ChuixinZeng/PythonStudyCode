# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

from core import _load_database
from core import _get_balance
from core import _get_shopping_history
from core import _top_up
from core import _save_account
from core import _shopping

# 自定义错误提示信息
_error_info = '输入有误，请检查后重新输入！'

# 定义一个函数login，用于登录系统
def _login():
    database = _load_database._load_database() # 加载数据库，使用的是前面定义好的加载数据库的函数
    blacklist = _load_database._load_database('../db/BlackList.json') # 设置用户的黑名单列表，在列表中的用户将不允许登录到购物系统
    print('欢迎登录购物系统！') # 打印欢迎信息
    # 第一个死循环
    while True:
        account = input("请输入您的账号登录系统（按q退出）：")
        if account in blacklist:
            # 如果账户在黑名单里面，则退出登录
            print("您的账号已经被锁定，请联系管理员处理！")
            _logout() # 直接调用下面定义好的_logout()函数
        # 判断如果用户输入的是q，就退出购物系统
        elif account == 'q':
            _logout()
        # 判断如果用户在数据库里面，则继续判断用户输入的密码是否正确
        # 这里使用while循环和count计数器，如果输入错误密码大于3次，则锁定账户
        elif account in database:
            count = 0
            while count < 3:
                pwd = input('请输入密码：')
                # 如果用户输入的密码和数据库保存的密码匹配
                if pwd == database[account]['pwd']:
                    # 进入到死循环
                    while True:
                        # 首先登录成功后，先获取用户账户的余额，告诉用户还剩多少钱，余额通过_get_balance函数得到
                        account_balance = _get_balance._get_balance(account)
                        # 高亮打印账户的余额信息
                        print('您的账户余额是\033[32m%d\033[0m'% account_balance)
                        # 让用户输入特定字母进入特定的菜单，并使用strip去除提示信息前后的空格
                        command = input('按h查询购物历史,按s开始购物,按t充值,开始购物后购物历史将被清空:').strip()
                        # 导入用户购物信息数据库
                        database = _load_database._load_database()
                        # 判断如果用户输入的是h，则查询购物历史
                        if command == 'h':
                            # 判断如果购物时间不为空的话，证明用户有购买历史
                            if database[account]['shopping_time'] != None:
                                # 加载函数_get_shopping_history，输出购物历史信息
                                _get_shopping_history._get_shopping_history(account)
                            else:
                                print('您在本商城没有购买过东西！')
                        elif command == 't':
                            # 如果用户输入的是t，则加载定义好的_top_up函数，执行充值操作
                            _top_up._top_up(account)
                        elif command == 's':
                            # 如果用户输入的是s，则将字典中的购物列表和时间初始化为空
                            # 注意：这个字典是从json文件转换过来的，里面有历史数据，所以需要先清空
                            # 等用户购物完成后，新的字典数据，即购物数据，会写回到json文件
                            database[account]['shopping_list'] = []
                            database[account]['shopping_time'] = None
                            # 调用_save_account函数，将清空的操作保存到database文件
                            _save_account._save_account(database)
                            # 调用shopping函数，开始购物
                            _shopping._shopping(account)
                        else:
                            # 如果用户的操作不符合上面所有的情况，则输出错误信息
                            # 这里直接调用前面定义好的_error_info函数，输出错误信息
                            print(_error_info)
                else:
                    count += 1
                    # 告诉用户还有多少次机会尝试登陆
                    print('输入的密码错误，你还有%s机会' % (3 - count))
            # 将用户账号添加至blacklist,保存成字典形式,value设置为None
            # 这里使用了字典的setdefalut用法，如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值
            blacklist.setdefault(account)
            # 用户输入三次错误操作之后，会跳出上面的while循环，然后打印信息告诉用户账号已锁定
            print('您的账号已经锁定！')
            # 将锁定的账户信息保存到黑名单列表
            _save_account._save_account(blacklist,'../db/BlackList.json')
            # 调用退出登录的函数
            _logout()
        else:
            print('账号不存在，请重试！或输入b返回上一层，输入q，退出购物程序！')

# 设置默认变量account = None来判定账号是否已经登录,如果没有登录就退出,则不打印购物信息
# 如果已经登录过，则打印购物历史信息
def _logout(account=None):
    if account != None:
        _get_shopping_history._get_shopping_history(account)
    exit('感谢您来购物!')
