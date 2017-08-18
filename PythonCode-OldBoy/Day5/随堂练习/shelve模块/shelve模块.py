# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# json解决了不同语言不同平台之间的数据交换
# pickle是Python独有的数据类型，支持所有Python的数据类型

# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
import shelve
import datetime
d = shelve.open('shelve_test')  # 打开一个文件


class aaa(object):
    def __init__(self, n):
        self.n = n


t = aaa(123)
t2 = aaa(123334)

info = {'age':22,'job':'it'}
name = ["alex", "rain", "test"]
d["name"] = name  # 持久化列表
d["t1"] = t  # 持久化类
d["t2"] = t2
d['info'] = info # 持久化dict
d['datetime'] = datetime.datetime.now() # 持久化时间


# 如果读取序列化之后的文件
print(d.get("name"))
print(d.get('info'))
print(d.get('datetime'))

'''
读取的结果：
['alex', 'rain', 'test']
{'age': 22, 'job': 'it'}
2017-08-18 16:32:31.007224
'''
d.close()