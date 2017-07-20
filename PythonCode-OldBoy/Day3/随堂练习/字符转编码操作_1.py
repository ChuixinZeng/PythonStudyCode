# -*- coding:gbk -*-

import sys
print(sys.getdefaultencoding()) # 默认格式


s = "你好"
s_gbk = s.encode('gbk')
print(s_gbk) # GBK
print("utf-8",s.encode()) # utf-8

# gbk转换成UTF8，具体过程是先转成Unicode，再由Unicode转成utf-8
gbk_to_utf8 = s_gbk.decode("gbk").encode('utf-8')
print("utf-8",gbk_to_utf8)