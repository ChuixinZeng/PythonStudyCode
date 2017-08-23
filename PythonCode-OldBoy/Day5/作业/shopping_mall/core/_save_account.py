# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

# 定义一个_save_account函数
# 用于将购物相关信息保存到JSON文件，比如购物时间，购物历史，购物列表，账户余额，创建的新用户和现有已存在用户信息
def _save_account(database, filename='../db/DataBase.json'):
    # 打开并可写文件,若文件已存在，则以前的内容将被清除
    # 使用with as语句的效率更高，不需要单独设置如何读文件之后再如何关闭文件，一个with as搞定所有读写关闭操作
    with open(filename,'w') as f: # f相当于一个变量，把打开并修改文件的操作赋予f
        json.dump(database,f) # json.dump是将一个Python数据类型列表进行json格式的编码解析
