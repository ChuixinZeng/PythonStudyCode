# -*- coding:utf-8 -*-

# Author:Chuixin Zeng


# python的logging模块提供了标准的日志接口，你可以通过它存储各种格式的日志，
# logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别，下面我们看一下怎么用。
import logging

logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")
logging.error('error log')
# 日志默认是有级别的，默认情况下info 和 debug是不输出的
logging.debug("debug message")
logging.info("info message")
# 输出
# WARNING:root:user [alex] attempted wrong password more than 3 times
# CRITICAL:root:server is down

# 可以手动把日志级别修改为自己需要的，比如改成debug级别
