# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import os
# 导入shutil模块，用于备份文件
import shutil
import time

# 定义查询函数，用于从员工信息表中查询信息
def search():
    user_search = input("请输入模糊查询的语句：").strip()
    # select name,age from staff_table where age > 22
    # select * from staff_table where dept = "IT"
    # select * from staff_table where enroll_date like "2013"
    # 将输入的条件语法以空格形式拆分成列表
    search_list = user_search.split(' ')
    #print(search_list)
    # 定义一个列表，用于保存查询结果
    found_info = []
    with open('staff_info.txt','r',encoding='utf-8') as f:
        for line in f:
            user_info = line.strip().split(',') # 循环读取员工信息
            # print(user_info)
            # ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
            # ['1', '张三', '25', '152015410', '运维', '2013-11-01']

            # 将查询条件字符串写入变量，这里的查询条件对应的是age > 22
            conditional = '%s %s %s' % (user_info[2],search_list[6],search_list[7])
            # print(conditional) # age > 22

            # 如果用户输入的查询表达式里面第六个元素是=，则替换成==
            # 因为查询条件有可能是：select name,age from staff_table where age = 25
            # 为了方便if判断，就需要把=替换成==
            if search_list[6] == '=': # 如果是等号就替换
                conditional = conditional.replace('=','==')

            # 用语句关键字匹配，用eval()将字符串转换为判断条件
            # 如果用户输入的查询表达式符合下面的条件
            if search_list[5] == 'age' and user_info[0].isdigit() and eval(conditional):
                # 则把用户信息表的name，age元素附加到存放查询结果的表格中
                found_info.append([user_info[1],user_info[2]])

            # 如果用户输入的查询表达式符合下面的条件
            # 查询语句里面包含元素dept，并且用户信息表的dept信息和查询表达式的dept信息匹配
            elif search_list[5] == 'dept' and user_info[4] in search_list[7]:
                # 则把user_info员工信息表的匹配行整个附加到found_info中
                found_info.append(user_info)
            # 通过用户输入的表达式中的enroll_date和用户信息表进行匹配，如果匹配上，则附加行到found_info表
            # 切片出用户信息列表中的年份与语法中的年份对比，年份只保留年，例如2017，切片后，去掉月日信息-11-01
            elif search_list[5] == 'enroll_date' and user_info[5][0:4] in search_list[7]:
                found_info.append(user_info)
        if not found_info:
            print("没有找到你要搜索的员工！\n")
        else:
            print("找到如下员工信息:\n")
            for i in found_info:
                print('|'.join(i))
            print("\n共计找到 %d 条信息\n" % len(found_info))
    return found_info

def add():
    user_add = input("请输入您要增加的员工信息（格式要求 zengchuixin,22,12378902792,IT）：").strip()
    add_list = user_add.split(",") # 用，号将用户输入的员工信息拆分为列表
    # print(add_list) # ['guoguoguo', '22', '12378902792', 'IT']
    phone = [] # 定义一个空列表
    with open('staff_info.txt','r+',encoding="utf-8") as f:
        user_id = 0 # 保存员工ID的变量，初始值0
        for line in f:
            user_info = line.strip().split(',')
            # print(user_info)
            # ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
            # ['1', '张三', '25', '152015410', '运维', '2013-11-01']

            # 把现有员工信息表中已经存在的phone的值追加保存到前面定义的phone列表里面
            phone.append(user_info[3])

            # 判断是否要给员工ID变量赋值，循环结束后，user_id的值就是最后一行员工信息的ID值
            if user_info[0].isdigit() and user_id < int(user_info[0]):
                user_id = int(user_info[0])

        # print(phone) # 打印查看追加后的phone列表，包含现有员工的phone信息
        # 这里判断增加的信息是不是存在，是以phone做唯一键进行判断的，如果phone不存在，则认为是新员工
        # 而且staff_id要自动增加，前面for循环里面的user_id保存了最后一行user_id的值
        # 如果通过phone判断员工信息不存在，则ID在此基础上+1
        if add_list[2] not in phone:
            f.write('\n'+str(user_id+1)+','+','.join(add_list))
            print("员工%s的信息已添加成功！\n" % add_list[0])
        else:
            print("您要添加的员工信息已经存在！\n")

def modify():
    user_mod = input("请输入修改员工信息的语法：").strip()
    # UPDATE staff_table SET dept = "Market" WHERE where dept = "IT"
    mod_list = user_mod.split()
    user_list = []
    mod_flag = False
    with open('staff_info.txt','r',encoding='utf-8') as f,\
        open('staff_info_new','w',encoding='utf-8') as f2:
        for line in f:
            user_info = line.strip().split(',')
            # 如果用户的dept和修改用户信息语法的dept的值匹配（实际是元素10）
            if user_info[4] in mod_list[10]:
                # 将标志位设置为true，如果不满足这个if的条件，则默认标志位为false
                mod_flag = True
                # 将修改语法中set的dept的值更新到user_info中的dept的值，即达到了修改dept的目的
                user_info[4] = mod_list[5].strip('"')
                print("员工%s 信息已修改！\n" % user_info[1])
            # 将修改过的员工信息表的所有内容附加到新的类别user_list
            user_list.append(user_info)
        # 从user_list列表里面循环读取每一行
        print(user_list)
        for list in user_list:
            # 如果list中的第一个元素不是数字，第一行肯定不是数字，是员工信息表的表头
            if not list[0].isdigit():
                # 将list内容逐行写入到新的文件中
                f2.write(','.join(list))
            else:
                # 如果是数字，则换行后，写入到新表，除了第一行，后续的行都是数字开头
                f2.write('\n'+','.join(list))
        if not mod_flag:
            print("没有找到要修改信息的员工！\n")
modify()