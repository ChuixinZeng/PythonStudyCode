# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 字符串实际上并不是修改了内容，而是更新后的内容把原来的内容全部覆盖了
# 列表可以嵌套列表，可以嵌套字典

name = "name zengchuixin zengchuxin"
print(name.capitalize()) # 首字符大写
print(name.count("a")) # 统计字符数量
print(name.center(50,"-")) # 字符串居中
print(name.endswith("ex")) # 判断字符串以什么结尾，比如判断邮件地址是不是以.com结尾
print(name.find("chui")) # 查找字符串的索引，name的开始索引是4，字符串也可以切片
print(name[name.find("name"):3]) # 字符串切片，取nam
print('ab123'.isalnum()) # 判断是不是阿拉伯数字加阿拉伯字符，返回值为true或false
print('abc123'.isalpha()) # 判断是不是纯英文字符
print('1A'.isdecimal()) # 判断是不是十进制
print('1A'.isdigit()) # 判断是不是整数
print('Abc'.isidentifier()) # 判断是不是一个合法的标识符，是不是一个合法的变量名
print('abc'.islower()) # 判断是不是小写
print('abc'.isnumeric()) # 判断是不是一个数字
print('abc'.isspace()) # 判断是不是空格
print('Abc'.istitle()) # 判断是不是标题（首字母大写
print('abc'.isprintable()) # 判断文件是否能打印，比如TTY终端文件，drivefile是无法打印的
print('abc'.isupper()) # 判断是不是大写
print('abc abc'.join("==")) # 奇葩的用法
print(','.join(["1", "2", "3"]))  # 将列表转换成字符串，并用,号隔开
print(name.ljust(50,"*")) # 如果长度不够50，在右边用*补充
print(name.rjust(50,"*")) # 如果长度不够50，在左边用*补充
print('ZENG'.lower()) # 把大写变成小写
print('zengchuixn'.upper()) # 把小写变成大写
print('\nAeng'.lstrip()) # 从左边去掉空格或回车
print('\nAzeng\n'.rstrip()) # 从右边去除空格或回车
print(' \nAxeng\n'.strip()) # 全部去除空格或回车
print('alex li'.replace('l','L',1)) # 替换第一个l为大写
print('alex li'.rfind('l')) # 返回的是最右边的l的下标
print('alex li'.split()) # 分割字符串，默认按照空格分割成列表了
print('alex li'.split('l')) # 分割字符串，按照l分，然后l被当成分割字符了
print('1+2+3+4'.split('+')) # 以+分割，提取字符串到列表里
print('1,2\n3,4'.splitlines())# 按照换行来分，在Linux上是\n，在Windows上是`n，这个可以自动识别不同系统的换行操作
print('alex li'.swapcase()) # 大写转小写，小写转大写
print('alex li'.title()) # 转换为title
print('alex li'.zfill(50)) # 不够50位的用0填充

p = str.maketrans("abcdef", '123456') # 把前面的字符串转换成后面的值，左右的值必须对应一样多
print("alex li".translate(p)) # 这里面a转成了1，e成了5，其他的因为没有，所以没转换


name4 = "my name is {name} and i am {year} old"
print(name4.format(name = 'zengchuixin',year = 29)) #格式化字符串
print(name4.format_map( {'name':'zengchuixin','year': 29} )) # 结合字典格式化字符串，和上一行效果一样

name1 = "zengchuixin \tzengchuxin"
print(name1.expandtabs(tabsize=30)) # 将字符串中的tab键\t转换成多少空格