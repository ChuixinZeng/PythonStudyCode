# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import copy
# 浅拷贝过来的对象只是对被拷贝的对象的引用
person = ["name", ["saving", 100]]

# 对person列表进行浅拷贝有三种方式
# 第一种
p1 = copy.copy(person)

# 第二种
p2 = person[:]

# 第三种
p3 = list(person)

# 浅拷贝的用处：p1和p2都是基于person拷贝来的，假设p1和p2是夫妻关系，他俩有一个共同的银行账号，但是名字不同
# 用来创建联合账户

p1 = person[:]
p2 = person[:]

p1[0] = 'alex'
p2[0] = 'tom'

p1[1][1] = 50
print(p1)
print(p2)




