# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 字典 dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# a. 请循环输出所有的 key
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
for i in dic.keys():
    print("key:",i)
# 请循环输出所有的 value
for i in dic.values():
    print("value:",i)

# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# Python 字典 setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic.setdefault("k4","v4")
print(dic)
#结果：{'k2': 'v2', 'k3': [11, 22, 33], 'k1': 'v1', 'k4': 'v4'}

# 请在修改字典中 “k1” 对应的值为 “alex”，输出修改后的字典
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic["k1"] = "alex"
print("修改K1的值：",dic)

# 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
b = list(dic["k3"])#读取k3的value,转换成list赋值给B
b.append(44)#将元素添加至列表B中
dic["k3"] = b#将列表赋值给k3的value
print("往字典中的列表里添加元素：",dic)

# 请在 k3 对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
b = list(dic["k3"])
b.insert(0,18)
dic["k3"] = b
print("往字典中的列表里面插入元素：",dic)

# 将列表 li = ["alex", "seven"] 转换成字典且字典的 key 按照 10 开始向后递增
li = ["alex", "seven"]
dict = {}
for i,name in enumerate(li,10):
    dict[i] = name
print(dict)
