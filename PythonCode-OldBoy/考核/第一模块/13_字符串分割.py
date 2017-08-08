# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 将 name 变量对应的值根据 “l” 分割，并输出结果

# 第一种方法
name = "alex"
name1 = name[:1]
name2 = name[-2:]
print(name1,name2)

# 第二种方法
name = " aleX"
for i,v in enumerate(name):
    if v == "l":
        print(name[:i],name[i+1:])
