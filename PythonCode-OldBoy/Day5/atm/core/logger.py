#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
处理所有的日志记录工作
'''

import logging
from conf import settings

def logger(log_type):

    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)


    # 创建控制台处理程序和调试级别
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # 创建文件处理程序并设置警告级别
    log_file = "%s/log/%s" %(settings.BASE_DIR, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
    # 'application' code
    '''logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')'''

