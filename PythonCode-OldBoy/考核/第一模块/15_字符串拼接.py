# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 利用下划线将列表的每一个元素拼接成字符串，li = ['alex', 'eric', 'rain']

# 方法一
li = ['alex', 'eric', 'rain']
b = li[0]+"_"+li[1]+"_"+li[2]
print(b)

# 方法二
li = ['alex', 'eric', 'rain']
c = ""
for i,name in enumerate(li,1):
    if i == len(li):#判断是否是最后一位
        c = c + name
    else:
        c = c + name + "_"
print(c)