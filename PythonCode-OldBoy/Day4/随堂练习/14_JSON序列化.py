# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 序列化就是把数据写入到硬盘的文件上，例如虚拟机做快照，用json的dumps，这是标准用法
import json

# def sayhi(name):
#     print("hello,",name)

# 把函数的内存地址写到info，然后用json进行dumps，会报错：TypeError: Object of type 'function' is not JSON serializable
# json用于不同语言之间的数据交互，只能用于字典，列表这种不同语言之间的简单转换
# 不同语言的类的特性和定义完全不同，所以太复杂了，没法干
# xml迟早会被JSON取代

info = {
    'name':'alex',
    'age':'22',
    #'func': sayhi
}
f = open('text.text','w')
#f.write(str(info))
f.write(json.dumps(info))
print(json.dumps(info))
f.close()