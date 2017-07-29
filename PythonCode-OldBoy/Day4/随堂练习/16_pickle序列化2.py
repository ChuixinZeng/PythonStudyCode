# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import pickle

def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':'22',
    'func': sayhi
}
f = open('text.text','wb')
# 下面的是另外一种用法，跟f.write(pickle.dumps(info))的意思是完全一样的
pickle.dump(info,f)

f.close()