# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# Iterable可迭代的
from collections import Iterable

# （1）可迭代对象iterable

# 判断列表、字典、字符串、数字、生成器是否可以迭代，是不是可迭代对象
print(isinstance([],Iterable)) # 可迭代
print(isinstance({},Iterable)) # 可迭代
print(isinstance('abc',Iterable)) # 可迭代
print(isinstance(100,Iterable)) # 不可迭代

print(isinstance((x for x in range(10)),Iterable))

# （2）迭代器Iterator

# 可迭代对象和迭代器不是一个东西，比如列表是可迭代对象，但不是迭代器
# 只要有next方法，就叫迭代器，下面的a就不是迭代器，因为没有next方法
a = [1,2,3]
print(dir(a))
# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了
# *可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

# 生成器都是迭代器，有next方法；但迭代器不一定是生成器
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))

# （3）把迭代器对象变为迭代器

a = [1,2,3]
print(iter(a))
b = iter(a)
print(b.__next__())
print(b.__next__())
print(b.__next__())

# (4)为什么list、dict、str等数据类型不是Iterator？
#
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
range(10) # 在Python 3.0上默认循环已经是迭代器，但是在Python2.x上面会执行出来，就不是

# （5）迭代器的用途
# 底层很多地方都在用，比如for循环，文件操作等
