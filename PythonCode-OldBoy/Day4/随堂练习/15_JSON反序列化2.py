# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
import json
# 反序列化就是把序列化存到硬盘的文件内容再加载回来,用json的loads，这是标准用法


info = {
    'name':'alex',
    'age':'22'
}
f = open('text.text','r')
# data = f.read()
# f.close()
# # print(eval(data)) # 加eval把str转为字典，非标准用法
data = json.loads(f.read())
# 在Python 2.x里面可以load多次，但在3.x里面只能load一次
# 最佳实践：写程序每次只dump一次，只load一次
print(data)

