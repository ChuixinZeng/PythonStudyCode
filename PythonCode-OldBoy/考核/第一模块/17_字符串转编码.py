# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 将字符串转换成 utf-8 编码的字节，并输出，然后将该字节再转换成 utf-8 编码字符串，再输出

n = "老男孩"
print(n.encode(encoding="utf-8"))
print(n.encode(encoding="utf-8").decode(encoding="utf-8"))
# 将字符串转换成 gbk 编码的字节，并输出，然后将该字节再转换成 gbk 编码字符串，再输出

n = "老男孩"
print(n.encode(encoding="gbk"))
print(n.encode(encoding="gbk").decode(encoding="gbk"))