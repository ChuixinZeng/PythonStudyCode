# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 元组只能切片，只能查，不能修改里面的值，又叫只读列表

names = ("alex", "jack", "tom")
# 元组只有下面两种用法
print(names.count([1]))
print(names.index("alex"))