# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 除了0，其他的都为真，下面是false
print(all([0,-1,3]))

# 只要列表有一个数据为真，就返回真，列表为空，就是false
print(any([0,-1,3]))

# 把列表打印成字符串形式
print(ascii([1,3,"开挂"]))
a = ascii([1,3,"开挂"])
print(type(a)) # 列表变成字符串了

