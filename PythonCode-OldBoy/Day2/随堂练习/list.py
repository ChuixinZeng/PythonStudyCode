# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

names = ["zengchuixin", "zengchuixin2", "zengchuixin3", "zengchuixin4"]

print(names)
print(names[0]) # zengchuixin所在的位置就是0
print(names[0], names[2])
# 取中间,顾头不顾尾，不能用1:2，否则不包括zengchuixin3
# 这个就叫切片
print(names[1:3])

# 取前三个位置
print(names[0:3])
print(names[:3])

# 取最后一个元素
print(names[-1])

# 取最后两个值，取值是从左往右数，而不是从右往左，为了防止顾首不顾尾导致最后一个值取不出来，所以：后面省略
print(names[-2:])

# 往列表里面追加放值
names.append("zengchuixin5")
print(names)

# 追加的值放到随意的位置



