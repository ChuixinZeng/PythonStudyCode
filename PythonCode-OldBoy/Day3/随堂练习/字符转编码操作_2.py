# -*- coding:gbk -*-

# 在文件头声明文件格式是GBK的，光改文件编码为GBK，但是不声明的话，会报错，默认执行程序的时候，还是utf-8

import sys
print(sys.getdefaultencoding()) # 默认格式


s = "你好" # 还是unicode，前面改的只是文件的编码，但是Python本身的数据类型就是Unicode，不会因为上面声明什么，就会改成什么

# 所以在s已经是Unicode情况下，就不需要再decode操作了，直接encode成gbk就行了
print(s.encode('gbk'))
print(s.encode('utf-8'))
# 把默认的Unicode转换成utf-，再把utf-8 decode encode为gb2312，是bytes形式显示 b'\xc4\xe3\xba\xc3'
print(s.encode('utf-8').decode('utf-8').encode('gb2312'))

# gb2312再转换成中文，这里是吧bytes转成中文字符串了

print(s.encode('utf-8').decode('utf-8').encode('gb2312').decode('gb2312'))