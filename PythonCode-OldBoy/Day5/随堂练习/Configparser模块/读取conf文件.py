# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 配置文件更多是需要去解析它，读取它，而很少需要去写入它
import configparser
conf = configparser.ConfigParser()

conf.read("example.ini")

#只打印除出了节点['bitbucket.org', 'topsecret.server.com']
print(conf.sections())

# 打印default下所有内容
print(conf.defaults())

# 读
print(conf['bitbucket.org']['user'])


########### 读 #
# has_section用来判断是否有特定的配置# ########
# secs = config.sections()
# print secs
# options = config.options('group2')
# print options

# item_list = config.items('group2')
# print item_list

# val = config.get('group1','key')
# val = config.getint('group1','key')

# ########## 改写 ##########
# sec = config.remove_section('group1')
# config.write(open('i.cfg', "w"))

# has_section用来判断是否有特定的配置
# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))


# config.set('group2','k1',11111)
# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')
# config.write(open('i.cfg', "w"))
