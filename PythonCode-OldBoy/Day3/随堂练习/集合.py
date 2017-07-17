# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

list_1 = [1, 4, 6, 5, 7, 9, 3, 7, 6]
list_1 = set(list_1)
print(list_1,type(list_1))
# 打印的结果如下，首先去重了，然后set代表打印的是一个集合，放在大括号里面
#{1, 3, 4, 5, 6, 7, 9} <class 'set'>
# 集合也是无序的，数据量大的时候能体现出来

list_2 = set([2,6,0,66,22,8])
print(list_1,list_2)
# 在list_1和list_2里面有交叉的内容

# 将交叉的内容取出来，就是取交集
print(list_1.intersection(list_2))

# 并集，两个列表合并起来，并且去掉重复的数
print(list_1.union(list_2))

# 差集，在我这有的，在你那没有，也就是list1有但是list2没有的
print(list_1.difference(list_2))

# 子集，判断list1是不是list2的子集，这里返回的是false
print(list_1.issubset(list_2))

# 这里返回的是true
# 反向差集，
list_3 = set([1,4])
print(list_3.issubset(list_1))

# 父集，判断list1是不是list2的父集，这里返回的是false
print(list_1.issuperset(list_2))

# 对称差集
# 把两个里面互相都没有的取出来放在一起
print(list_1.symmetric_difference(list_2))

# 代表list3和list4没有交集的情况下，返回true，有交集返回false
list_4 = ([5,6,8])
print(list_3.isdisjoint(list_4))

print('-------------运算符来表达关系测试------------------')

# 交集，无顺序要求
print(list_1 & list_2)

# 并集，无顺序要求
print(list_1 | list_2)

# 差集
print(list_1 - list_2)

# 对称差集，无顺序要求

print(list_1 ^ list_2)

print('-------------集合操作------------------')

# 往集合中添加
list_1.add(999)
print(list_1)

# 添加多项
list_1.update([10,11,12])
print(list_1)

# 删除,集合是天生去重的，所以不会存在删除重复项的问题
list_1.remove(999)
print(list_1)

# 列表长度
print(len(list_1))

# 列表、字典、集合、字符串都是下面这种判断的写法
print(9 in list_1)

# 删除并返回删除的元素，属于随机删除，没法指定确切的值，指定确切的值删除用remove
print(list_1.pop())

# 执行完了之后，不管要删除的值是不是存在，都不会返回值，不会返回成功或失败的结果
# 但是如果使用remove的话，遇到集合里面不存在的元素，就会报错
print(list_1.discard(4))