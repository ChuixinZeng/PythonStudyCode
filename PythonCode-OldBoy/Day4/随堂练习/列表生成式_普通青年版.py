# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 列表[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],我要求你把列表里的每个值加1

# 方法一
a = [0,1,2,3,4,5,6,7,8,9]
b = []
for i in a:
    b.append(i+1)
print(b)

# 方法二
c = [0,1,2,3,4,5,6,7,8,9]
for index,i in enumerate(c):
   c[index] += 1
print(c)