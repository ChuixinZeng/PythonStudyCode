# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个 key 中，将小于 66 的值保存至第二个 key 的值中。
#
# 即: {'k1': 大于 66 的所有值, 'k2': 小于 66 的所有值}
li = [11,22,33,44,55,66,77,88,99]
l1 = []
l2 = []
for i in li:
    if i >66:
        l1.append(i)
    else:
        l2.append(i)
dict = {"k1":l1,"k2":l2}
print(dict)