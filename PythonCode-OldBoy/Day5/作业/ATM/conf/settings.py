# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库放在ATM文件夹下面的DB文件夹里面
# 目前是文件形式存储，文件名是accounts
DATABASE = {
    'engine':'file_storage',
    'name':'accounts',
    'path':"%s/db" % BASE_DIR
}

# 日志级别是info级别
LOG_LEVEL = logging.INFO
# 两种日志类型：交易日志和访问日志
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

# 交易日志类型：repay还款/withdraw取现/transfer转账/consume消费
# 交易利息interest
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}

