# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
"""
type()用于查看数据类型
2**32代表是2的32次方
在Python2里面分int整型和long长整型，而Python3里面只有int整型
在JAva里面超了会报错
"""
# 字符串转二进制

msg = "我爱北京天安门"
print(msg)

# 转二进制

print(msg.encode(encoding="utf-8")) # 在Python3里面如果encode后面不写编码格式，则默认就是utf-8，在Python2里面默认使用系统编码格式

print(msg.encode(encoding="utf-8").decode(encoding="utf-8")) # 可以吧二进制转换成字符串
