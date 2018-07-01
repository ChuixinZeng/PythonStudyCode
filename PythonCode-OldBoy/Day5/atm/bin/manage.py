#-*- Coding:utf-8 -*-

import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(base_dir)
sys.path.append(base_dir)

# 管理端(提供管理接口，包括添加账户、用户额度，冻结账户)
from core import accounts
from core import transaction

# 解冻账户
def unblock_account(acc_data):
    user_input = input("请输入你要解冻的用户：")
    flag = 0
    # 锁定用户
    val = transaction.lock_or_not(user_input,flag)
    if val == 0:
        print("解冻成功！")
        return

# 冻结账户
def block_account(acc_data):
    '''
    冻结账户初步构想是，在linux里把他的权限改掉;
    或者将其文件改名
    :param acc_data:
    :return:
    '''
    user_input = input("请输入你要冻结的用户：")
    flag = 1
    #锁定用户
    val = transaction.lock_or_not(user_input,flag)
    if val == 0:
        print("冻结成功！")
        return

# 添加账户、用户额度
def add_account(acc_data):
    account = {
        "id": None,
        "balance": None,
        "expire_date": None,
        "enroll_date": None,
        "credit": None,
        "pay_day": None,
        "password": None,
        "status": None
    }
    menu = {
        0: "账户（数字）:",
        1: "余额:",
        2: "到期时间:",
        3: "办卡时间:",
        4: "信用额度:",
        5: "还款日期:",
        6: "密码:",
        7: "默认:"}
    menu_user = {
        0: "id",
        1: "balance",
        2: "expire_date",
        3: "enroll_date",
        4: "credit",
        5: "pay_day",
        6: "password",
        7: "status"
    }
    for i in range(8):
        data = input("%s" % menu[i]).strip()
        account['%s' % menu_user[i]] = data
    accounts.dump_account(account)#写入文件
    print("创建成功！")
    return



def logout(acc_data):
    exit("程序退出！")
# 管理界面主程序
def manage_main(acc_data):

    menu = u'''
    ---------管理界面---------
    1.添加账户
    2.冻结账户
    3.解冻账户
    4.退出'''
    menu_dic = {
        '1': add_account,
        '2': block_account,
        '3': unblock_account,
        '4': logout
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input("请输入你的选择：")
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1m选择不存在！\033[0m")