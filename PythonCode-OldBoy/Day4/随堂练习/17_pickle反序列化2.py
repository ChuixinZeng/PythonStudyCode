# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import pickle

# dump多次
def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':'22'
}
f = open('text.text','rb')

data = pickle.load(f) # 相当于data = pickle.loads(f.read())
print(data)

