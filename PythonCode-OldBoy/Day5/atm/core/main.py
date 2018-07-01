#!_*_coding:utf-8_*_

'''
主程序句柄模块，处理所有用户交互的内容

'''

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#print(base_dir)
sys.path.append(base_dir)

from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required
from shopping_mall import shopping_mall
from bin import manage
import time


#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')


# 临时帐户数据，只保存内存中的数据
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None

}

def account_info(acc_data):
    print(user_data)

@login_required
def repay(acc_data):
    '''
    打印当前余额，让用户偿还账单
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    #for k,v in account_data.items():
    #    print(k,v )
    current_balance= ''' --------- 账户信息 --------
        账户金额 :    %s
        余额:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;输入你要还款的金额:\033[0m").strip()
        if len(repay_amount) >0 and repay_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)
            if new_balance:
                print('''\033[42;1m新的账户:%s\033[0m''' %(new_balance['balance']))
                print('''输入b可退出''')

        else:
            print('\033[31;1m[%s] 不是一个有效的数目, 只接受整数!\033[0m' % repay_amount)
            print('''输入b可退出''')

        if repay_amount == 'b':
            back_flag = True
def withdraw(acc_data):
    '''
    打印当前余额，让用户执行取款操作
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance= ''' --------- 账户信息 --------
        账户金额 :    %s
        余额:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1m请输入取款的金额:\033[0m").strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1m新的账户:%s\033[0m''' %(new_balance['balance']))
                print('''输入b可退出''')

        else:
            print('\033[31;1m[%s]不是一个有效的数目, 只接受整数!\033[0m' % withdraw_amount)
            print('''输入b可退出''')

        if withdraw_amount == 'b':
            back_flag = True

#转账
@login_required
def transfer(acc_data):
    '''
    打印当前余额,转账操作函数
    :param acc_data:用户数据
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    # 将用户账户名字传入到load_current_balance中
    # 返回最新的用户数据赋值给 account_data
    current_balance = ''' --------- 银行信息 --------
    信用额度: %s
    账户余额: %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        reciprocal_account = input("\033[31;1m请输入对方帐户名：\033[0m").strip()  # 输入对方账户
        transfer_amount = input("\033[31;1m转账金额：\033[0m").strip()  # 转账金额
        if reciprocal_account or transfer_amount == 'b':
            return
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'transfer',
                                                       transfer_amount, re_account=
                                                       reciprocal_account)
            if new_balance:
                print("\033[41;1m转账成功！\033[0m")
                print("\033[42;1m您当前的余额为:%s\033[0m" % (new_balance["balance"]))
            else:
                print('\033[31;1m去你大爷的\033[0m')

#账单
@login_required
def pay_check(acc_data):
    pass

#退出
def logout(acc_data):
    exit("程序已退出！")

#购物商城
def shopping_mall_this(acc_data):
    shopping_mall.main_menu(acc_data)
#管理窗口
def goto_manage():
   manage.manage_main(user_data)

def interactive(acc_data):
    '''
    与用户交互
    :return:
    '''
    menu = u'''
    ------- DAG5银行 ---------
    \033[32;1m1.  账户信息
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            print('accdata',acc_data)
            #acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1m输入的选项不存在，请重新输入!\033[0m")

# 带有购物商场的主菜单
def main_menu(acc_data):
    main_menu = u'''
    ----------主菜单---------
    \033[32;1m
    1.购物商城
    2.银行卡操作
    3.退出
    \033[0m
    '''
    main_menu_dic = {
        '1':shopping_mall_this,
        '2':interactive,
        '3':logout,
    }
    exit_flag = False
    while not exit_flag:
        print(main_menu)
        user_option = input("请输入你的选择：").strip()
        if user_option == 'b':
            return
        if user_option in main_menu_dic:
            main_menu_dic[user_option](acc_data)
        else:
            print("\033[31;1m选择不存在！\033[0m")

def run():
    '''
    当程序启动时，这个函数将被调用，这里处理用户交互的东西
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        # interactive(user_data) # 这是ATM银行卡操作的入口，这里注释掉，把入口统一到下面的main_menu中
        main_menu(user_data)