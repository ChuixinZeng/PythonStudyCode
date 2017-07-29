# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import json

# def sayhi(name):
#     print("hello,",name)

info = {
    'name':'alex',
    'age':'22',
    #'func': sayhi
}
f = open('text.text','w')
f.write(json.dumps(info))
# 在Python 2.x和3.x里面可以dump多次，但是这样做没有啥意义，建议：
# 最佳实践：写程序每次只dump一次，只load一次
info['age'] = 21
f.write(json.dumps(info))

f.close()