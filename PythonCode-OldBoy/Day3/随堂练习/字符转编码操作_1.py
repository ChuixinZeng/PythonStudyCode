import sys
print(sys.getdefaultencoding())

s = "ฤ๚บร"
s_gbk = s.encode('gbk')
print(s_gbk)
print(s.encode())
