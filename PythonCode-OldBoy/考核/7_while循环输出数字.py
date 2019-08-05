# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 使用 while 循环实现输出 1，2，3，4，5， 7，8，9， 11，12
i = 1
while i < 13:
    if i == 6 or i == 10:
        pass
    else:
        print(i)
    i += 1