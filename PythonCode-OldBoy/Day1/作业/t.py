# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Time:2016-08-16 23:40
#---------------
# 编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
#-----------------

userdict = {}
wuserdata = []
chushihua
_num = 0
print("欢迎来到Python系统，请先登录")

while True:
    username = input("用户名:")
    password = input("密码:")
    #读取用户登陆文件
    user_data = open('user.txt')
    for data in user_data:
        userlist = data.strip()
        userdata = userlist.split(',')
        user_name = userdata[0].strip()
        user_passwd = userdata[1].strip()
        user_lock = userdata[2].strip()
        user_error_num = int(userdata[3].strip())
        userdict[user_name] = {'username':user_name,'password':user_passwd,'lock':user_lock,'errornum':user_error_num}
    user_data.close()

    #判断用户账户是否合法
    if username in userdict.keys():
        if userdict[username]['lock'] == '1':
            print('该账户已被锁定,请联系管理员')
            break
        #判断用户名密码是否匹配
        if username == userdict[username]['username'] and password == userdict[username]['password']:
            print("Success! 登录成功，欢迎",username)
            break
        else:
            userdict[username]['errornum'] += 1
            if userdict[username]['errornum'] >= 3:
                print('帐号密码输入错误3次，被锁定，退出')
                userdict[username]['lock'] = 1
                userdict[username]['errornum'] = 0
            else:
                print('帐号密码错误')
            wirte_data = open('user.txt','w+')
            for t in userdict.values():
                wuserdata = [t['username'],t['password'],str(t['lock']),str(t['errornum'])]
                wuserdatestr = ','.join(wuserdata)
                wirte_data.write(wuserdatestr + '\n')
            wirte_data.close()
            if userdict[username]['errornum'] >= 3:
                break
    else:
        print('帐号或密码错误')



