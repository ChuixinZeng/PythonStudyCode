# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import logging

from logging import handlers

logger = logging.getLogger(__name__)

log_file = "timelog.log"
# 按数量最大保留3个
fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3,encoding="utf-8")
# 下面是按时间进行截断，S代表秒
# fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3)
'''
when参数是一个字符串。表示时间间隔的单位，不区分大小写。它有以下取值：
S 秒
M 分
H 小时
D 天
W 每星期（interval==0时代表星期一）
midnight 每天凌晨
'''

formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)

# 可以导入时间模块，来测试通过时间截断日志功能
#　import time

logger.warning("test1")
# time.sleep(2)
logger.warning("test12")
# time.sleep(2)
logger.warning("test13")
# time.sleep(2)
logger.warning("test14")