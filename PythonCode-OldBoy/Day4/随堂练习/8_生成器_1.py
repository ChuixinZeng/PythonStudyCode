# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 生成器跟列表的区别：只有在调用时才会生成相应的数据，调用到哪一步就产生哪一步的数据
# 生成器取具体的值得时候，只记得当前的位置，不能往回退，不能跳着走
# 只有一个__next__方法，在Python2.7里面是next()

n = (x * x for x in range(10))
print(n) # 并没有生成数据，只是指向了一个内存地址

print(n.__next__()) # 取第一个值
print(n.__next__()) # 取第二个值
#n[10] # 无法打印结果，因为还没有生成列表
# 用循环一次性取其他值
for i in n:
    print(i)