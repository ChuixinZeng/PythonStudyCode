#!_*_coding:utf-8_*_
#__author__:"Alex Li"

from conf import settings
from core import accounts
from core import logger
#transaction logger



def make_transaction(log_obj,account_data,tran_type,amount,**others):
    '''
    处理所有用户的事务，公用的接口，例如存款、取款、还款等操作
    :param account_data: 用户账户数据
    :param tran_type: 交易类型
    :param amount: 交易金额
    :param others: 预留的扩展
    :return: 返回最新的数据
    '''
    amount = float(amount)
    if tran_type in  settings.TRANSACTION_TYPE:
        # 计算利息
        interest =  amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest

            # 转账操作
            if others.get('re_account'):
                re_account_data = accounts.load_current_balance(others.get('re_account'))
                re_account_balance = re_account_data['balance'] + amount  # 得到转入账户余额的最新值
                re_account_data['balance'] = re_account_balance  # 将最新的余额全部写入账户的余额中
                print(re_account_data)
                accounts.dump_account(re_account_data)  # 将最新的账户所有数据写入到文件中
            elif new_balance <0:
                print('''\033[31;1m你的账户 [%s] 没有足够的金额用于此次交易 [-%s], 你当前的账户是：
                [%s]''' %(account_data['credit'],(amount + interest), old_balance ))
                return

        account_data['balance'] = new_balance
        accounts.dump_account(account_data) # 保存新的账户信息到文件中
        log_obj.info("account:%s   action:%s    amount:%s   interest:%s" %
                          (account_data['id'], tran_type, amount,interest) )
        return account_data
    else:
        print("\033[31;1m交易类型 [%s] 不存在!\033[0m" % tran_type)

def lock_or_not(account,flag):
    data = accounts.load_current_balance(account)

    if data['status'] == 1:
        print("该账户已被锁定")
    elif data['status']:
        data['status'] = flag
        accounts.dump_account(data)
        return 0