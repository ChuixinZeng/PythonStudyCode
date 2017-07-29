# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import pickle

# 正常情况下下面的def不应该这样用，这里只是为了演示
# 下面的函数和序列化中的函数虽然名字一样，但是其实不代表一样的内容，这里只是函数名一样
def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':'22'
}
f = open('text.text','rb')
data = pickle.loads(f.read())
print(data)

