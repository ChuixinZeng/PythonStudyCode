
# -*- coding: UTF-8 -*-

# ordereddict标准库里面的模块，结合了字典和列表的特点，可以有序的输出字典信息

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")