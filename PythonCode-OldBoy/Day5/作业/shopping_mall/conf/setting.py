# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
import logging
from core import login

def setlog():
    logging.basicConfig(filename='../log/access.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(filename)s:%(lineno)d - %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug('用户登录日志')

setlog()