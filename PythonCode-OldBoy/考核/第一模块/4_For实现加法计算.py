# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 使用for循环和range实现输出 1-2+3-4+5-6...+99 的和

b = 0 #结果
for i in range(1,100):
    if i%2 == 0:#判断是偶数
        b = b - i #结果加当前的i
    else:#基数
        b = b + i #结果减当前i
    i += 1 #判断完自增一
print(b)
#结果：50