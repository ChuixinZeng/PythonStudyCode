# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 将 name 变量对应的值变大写，并输出结果
name = "aleX"
print("name1:",name.upper())
# 将 name 变量对应的值变小写，并输出结果
print("name2:",name.lower())

# 请输出 name 变量对应的值的前 3 个字符?
print("name3:",name[:3])

# 请输出 name 变量对应的值的后 2 个字符?
print("name4:",name[-2:])

# 请输出 name 变量对应的值中 “e” 所在索引位置?
for i,v in enumerate(name):
    if v == "e":
        print("e的索引是：%s" %i)

# 字符串是否可迭代?如可以请使用 for 循环每一个元素?
for i in name:
    print("字符串迭代：",i)

# li = ['alex', 'eric', 'rain'] a. 计算列表长度并输出
li = ['alex', 'eric', 'rain']
print("计算列表长度:",len(li))

# 列表中追加元素 “seven”，并输出添加后的列表
li = ['alex', 'eric', 'rain']
li.append("seven")
print("列表中追加元素：",li)

# 请在列表的第 1 个位置插入元素 “Tony”，并输出添加后的列表
li = ['alex', 'eric', 'rain']
li.insert(0,"seven")
print("列表中插入元素：",li)

# 请修改列表第 2 个位置的元素为 “Kelly”，并输出修改后的列表
li = ['alex', 'eric', 'rain']
li[1] = "Tony"
print("列表中修改元素：",li)

# 请删除列表中的元素 “eric”，并输出修改后的列表
li = ['alex', 'eric', 'rain']
li.remove('eric')
print("列表中删除元素：",li)

# 请删除列表中的第 2 个元素，并输出删除的元素的值和删除元素后的列表
li = ['alex', 'eric', 'rain']
print("删除列表中的第二个元素并打印删除的元素：",li.pop(1))

# 请删除列表中的第 3 个元素，并输出删除元素后的列表
li = ['alex', 'eric', 'rain']
li.pop(2)
print("删除列表中的第三个元素并打印剩余元素：",li)

# 请删除列表中的第 2 至 4 个元素，并输出删除元素后的列表
li = ['alex', 'eric', 'rain','Tony']
for i in range(3):
    li.pop(1)
print("循环删除第2到第4个元素",li)

# 请将列表所有的元素反转，并输出反转后的列表
li = ['alex', 'eric', 'rain']
print("反转列表：",list(reversed(li))) # reversed()函数返回的是一个迭代器，而不是一个List，需要再使用List函数转换一下

# 请使用 for、len、range 输出列表的索引
li = ['alex', 'eric', 'rain','Tony']
for i in range(len(li)):
    print("输出列表索引：",i)

# 请使用 enumerate 输出列表元素和序号(序号从 100 开始)l. 请使用 for 循环输出列表的所有元素
li = ['alex', 'eric', 'rain','Tony']
for i,name in enumerate(li,100): # enumerate可以接收第二个参数，用于指定索引起始值
    print(i,name)

# 有如下列表，请按照功能要求实现每一个功能li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
name = str(li[2][1][1])
print("从复杂列表里面取数：",name.capitalize())

# 请使用索引找到 'all' 元素并将其修改为 “ALL”
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
name = str(li[2][2])
print("从复杂列表里取数并转换大写：",name.upper())

# 有如下元组，按照要求实现每一个功能tu = ('alex', 'eric', 'rain')
# 计算元组长度并输出
tu = ('alex', 'eric', 'rain')
print("计算元组的长度：",len(tu))

# 获取元组的第 2 个元素，并输出
print("获取元组的第二个元素：",tu[1])

# 获取元组的第 1-2 个元素，并输出
print("获取元组的前两个元素：",tu[:2])

# 请使用 for 输出元组的元素
for i in tu:
    print("循环打印tu元组的元素：",i)

# 请使用 for、len、range 输出元组的索引
for i in range(len(tu)):
    print("循环打印元组的索引：",i)

# 请使用 enumrate 输出元祖元素和序号(序号从 10 开始)
for i,name in enumerate(tu,10):
    print(i,name)

# 请问 tu 变量中的"k2"对应的值是什么类型?是否可以被修改?如果可以，请在其中添加一个元素 “Seven”
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
b = tu[1][2]["k2"]
b.append("Seven")
print("往元组里内嵌的列表插入元素：",tu)

# 请问 tu 变量中的"k3"对应的值是什么类型?是否可以被修改?如果可以，请在其中添加一个元素 “Seven”
# 答：元组，可以，重新给k3赋值
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
b = list(tu[1][2]["k3"])#k3的value转换list
b.append("seven")#往字典添加值
tu[1][2]["k3"] = tuple(b)#给k3赋值
print(tu)

# 将字符串 s = "alex" 转换成列表
s = "alex"
print("将字符串转换成列表：",list(s)) # 结果是：['a', 'l', 'e', 'x']

# 将字符串转换成元组
s = "alex"
print("将字符串转换成元组：",tuple(s))

# 将列表转换成元组
li = ["alex", "seven"]
print("将列表转换成元组：",tuple(li))

# 将元组转换成列表
tu = ('Alex', "seven")
print("将元组转换成列表:",list(tu))

