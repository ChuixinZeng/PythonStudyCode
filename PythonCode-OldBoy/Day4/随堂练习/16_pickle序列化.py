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
#f.write(str(info))
f.write(pickle.dumps(info))
# 写完的数据看着像乱码，但不是乱码，是pickle的格式
print(pickle.dumps(info))
# 或者用下面的
pickle.dump(info.f)
f.close()