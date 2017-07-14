# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
'''
names = ["zengchuixin", "zengchuixin2", "zengchuixin3", "zengchuixin4"]

print(names)
print(names[0]) # zengchuixin所在的位置就是0
print(names[0], names[2])
# 取中间,顾头不顾尾，不能用1:2，否则不包括zengchuixin3
# 这个就叫切片
print(names[1:3])

# 取前三个位置
print(names[0:3])
print(names[:3])

# 取最后一个元素
print(names[-1])

# 取最后两个值，取值是从左往右数，而不是从右往左，为了防止顾首不顾尾导致最后一个值取不出来，所以：后面省略
print(names[-2:])

# 往列表里面追加放值
names.append("zengchuixin5")
print(names)

# 追加的值放到随意的位置
# 放在zengchuixin2的前面，就写zengchuixin2所在的位置
names.insert(1, "zengchuixina")
names.insert(3, "zengchuixinb")
print(names)

# 修改，替换zengchuixin2为zengchuixinc
names[2] = "zengchuixinc"
print(names)

# 删除有三种方法

names.remove("zengchuixinc")
print(names)

del names[2]
print(names)

# 删掉最后一个
names.pop() # 如果后面加上下标，例如names.pop(2) 就相当于 del names[2]
print(names)

# 在列表中找出某个人，假如列表人非常多，怎么快速找
# 知道具体的名称，通过把名字传递给列表，找到该名字所在的位置
print(names.index("zengchuixina"))
# 找到值所在的序号之后，可以把这个值输出打印
print(names[names.index("zengchuixina")])

# 清空列表
names.clear()
print(names)

# 列表里可以有重名的人
names = ["dengchuixin", "zengchuixin","aengchuixin2", "zengchuixin3", "zengchuixin4"]
print(names)
# 统计列表有多少重复的人
print(names.count("zengchuixin"))

# reverse反转列表
names.reverse()
print(names)

# sort方法用于排序，默认按照特殊符号、数字、大写、小写的顺序进行排序，按照ASCII吗的方式
names.sort()
print(names)

# 扩展列表,将另外一个列表合并到当前列表
names2 = [1,2,3,4]
names.extend(names2)
print(names)
print(names2)

# 删除列表
del names2
print(names2)
'''

'''
# 拷贝列表
names = ["dengchuixin", "zengchuixin",["alice","jack"],"aengchuixin2", "zengchuixin3", "zengchuixin4"]
names3 = names.copy() # 浅拷贝，只复制第一层列表，子列表相当于一个独立的内存地址，被直接拷贝了
print(names)
print(names3)

# 修改names列表，names3不会跟着一起修改
names[4] = "tom"
# 列表里面可以再包含子列表，修改子列表里面的值
names[2][1] = "zeng"
print(names)
print(names3)
'''
names = ["dengchuixin", "zengchuixin",["alice","jack"],"aengchuixin2", "zengchuixin3", "zengchuixin4"]
# 深拷贝，使用拷贝模块即可
import copy
# names3 = copy.copy(names) # 还是浅拷贝
names3 = copy.deepcopy(names) # 深度拷贝，完全克隆
print(names)
print(names3)

# 修改names列表，names3不会跟着一起修改
names[4] = "tom"
# 列表里面可以再包含子列表，修改子列表里面的值，大多数情况下不需要使用深拷贝，占内存空间
names[2][1] = "zeng"
print(names)
print(names3)

# range (1,10,2) 跳着循环打印
# 跳着切片，每隔一个取一个值
print(names[0:-1:2])
# 因为0和-1可以省略掉，所以上面的可以改成
print(names[::2])
# 打印从0到-1所有的值
print(names[:])
# 列表的循环
for i in names:
    print(i)












