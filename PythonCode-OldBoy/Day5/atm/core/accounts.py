#!_*_coding:utf-8_*_

import json
import time

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(base_dir)
sys.path.append(base_dir)

from core import db_handler
from conf import settings


def load_current_balance(account_id):
    '''
    返回帐户余额和其他基本信息
    :param account_id:
    :return:
    '''
    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_id)
    #
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account_id)

    return data

    # with open(account_file) as f:
    #     acc_data = json.load(f)
    #     return  acc_data
def dump_account(account_data):
    '''
    在更新了交易或帐户数据之后，将其转储到文件db
    :param account_data:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'],account_data=account_data)

    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_data['id'])
    # with open(account_file, 'w') as f:
    #     acc_data = json.dump(account_data,f)

    return True