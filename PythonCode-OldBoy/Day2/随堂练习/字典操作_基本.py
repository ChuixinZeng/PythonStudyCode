# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 键值对应的关系，前面是键，后面是值，字典是无序的，唯一的
# 无序是因为没有下标，不需要下标，因为有key，通过键key去找就行了
info = {
    'stu1101': 'TengLan Wu',
    'stu1102': 'LongZe LuoLa',
    'stu1103': 'XiaoZe Maliya',
}
print(info)
# 通过键从字典中取值，查找；这属于精确查找，如果不知道确切的键就没法查
print(info.get('stu1104'))
print(info['stu1101'])
# 修改字典里面键的值
info['stu1101'] = '武藤兰'
print(info['stu1101'])
# 往字典里面 添加值
info['stu1104'] = 'CangJingKong'
print(info['stu1104'])
# 删除字典里面的值，方法一
del info['stu1101']
print(info)
# 删除字典里面的值，方法二
info.pop('stu1102')
print(info)
# 随机删除字典里面的值
#info.popitem()
#print(info)

info1 = {
    'stu1101': 'TengLan Wu',
    'stu1102': 'LongZe LuoLa',
    'stu1103': 'XiaoZe Maliya',
}

# 更高级的查找方法，这种方法，有就返回值，没有就返回空，也不会报错
print(info1.get('stu1104'))
# 判断字典里面有没有数据，在就取，不在就创建一个，返回值是false代表没有，true代表有
print('stu1104' in info1) # info.has_key("1103")这是Python2的用法

b = {
    'stu1101':"Alex",
    1:3,
    2:5
}
# 把两个字典b和info1合并，有交叉就更新，没有就创建
info1.update(b)
print(info1)

#把字典转成了列表和元组
print(info1.items())

# 初始化一个新的字典，如果是多层就产生下面的现象
c = dict.fromkeys([6,7,8],[1,{"name": "alex"},444])
print(c)
c[7][1]["name"] = "Jack Chen" # 并不能只更新7所在的数据，而是6,7,8对应的全更新了，相当于三个key共享了后面一个值
print(c)
# print(info1.items())

info2 = {
    'stu1101': 'TengLan Wu',
    'stu1102': 'LongZe LuoLa',
    'stu1103': 'XiaoZe Maliya',
}
# 从字典里面循环取数据,这个效率更高
for i in info2:
    print(i, info2[i]) # i代表只打印key，而info[i]是打印值，二者放在一起就是打印键值
# 第二种方式，效率不如上面的高，items相当于把字典变成列表了，如果数据量大的话，光转换成列表就很长时间，慎用
for k,v in info2.items():
    print(k,v)