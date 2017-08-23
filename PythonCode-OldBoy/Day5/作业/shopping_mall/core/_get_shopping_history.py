# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

from core import _load_database
from core import _get_datetime
# 定义一个函数_get_shopping_history，用于查询购物历史记录
def _get_shopping_history(account):
    database = _load_database._load_database()
    history = database[account]['shopping_list']
    # 增加一个空列表,配合下边for循环将购物清单中的重复项合并
    aa = []
    for i in history:
        # 将购物车里面的shopping list和aa空列表进行对比，如果列表里面没有，就添加到列表
        # 也就意味着，如果列表已经有了就不添加了，达到了购物车去重的功能
        if i not in aa:
            aa.append(i)
    # 然后循环遍历aa列表里面的购物清单
    for j in aa:
        # 统计购买的每件商品的数量，也就是aa列表里面每件商品的数量，数量从history原始列表里面取（未去重的列表）
        count = history.count(j)
        # 统计购买商品的日期，日期就是account字典对应的商品的日期
        date = _get_datetime._get_datetime(account)
        # 打印购买的商品的数量、日期和商品名称
        print('您于%s购买了%s件%s' %(date,count,j))