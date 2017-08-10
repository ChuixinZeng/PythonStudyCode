# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import os
# 导入shutil模块，用于备份文件
import shutil
import time

# 定义一个装饰器，用于备份员工信息表
# 这个装饰器是在全部功能实现以后，额外添加的，实现不修改函数的内容，不修改函数的调用方式，对用户透明

def staff_info(func_type):
    def backup(func):
        def re_name(*args,**kwargs):
            # 如果func_type传入的参数值不是search_type，但是当前的操作不是查询，而是修改、删除或添加
            # 这种情况下，代表文件有改动过，就需要对改动前的staff_info.txt文件先进行备份
            if func_type != 'search_type':
                backup_time = time.strftime('%Y%m%d_%H%M%S')
                shutil.copyfile('staff_info.txt','staff_info_%s.bak' % backup_time)
                print("原始员工信息表已备份为 staff_info_%s.bak" % backup_time)
            print("已有员工信息如下：")
            # 备份完成之后，将当前员工信息表的内容打印出来
            with open('staff_info.txt','r',encoding='utf-8') as f:
                for line in f:
                    line = line.strip().split(',')
                    print('|'+'|'.join(line)+'|')

            # 上面备份完了之后，下面res的内容是执行被装饰的函数，然后再执行文件重命名
            # 后面加的*args **kwargs表示函数有参数就传进来，没参数就是空，比较灵活
            res = func(*args,**kwargs) # 这一句的func实际上是被装饰的函数

            # 如果func_type传入的值是mod_type或者del_type，代表是修改或删除了文件，这个时候做下面的操作：
                # 1. 因为原始的staff_info.txt文件已经备份过，所以这时候可以把原始文件删除掉了
                # 2. 将函数中新生成的staff_info_new文件改名为staff_info.txt，代表最终删除或修改完成
            if func_type in ['mod_type','del_type'] and os.path.exists('staff_info_new'):
                os.remove('staff_info.txt')
                os.rename('staff_info_new','staff_info.txt')
            return res # 返回res的内存地址
        return re_name # 返回re_name的内存地址，实际上该函数包含重命名和备份文件
    return backup

# 定义查询函数，用于从员工信息表中查询信息
@staff_info(func_type='search_type')
def search():
    user_search = input("请输入模糊查询的语句：").strip()
    # select name,age from staff_table where age > 22
    # select * from staff_info where dept = "IT"
    # select * from staff_info where enroll_date like "2013"
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

@staff_info(func_type='add_type')
def add():
    user_add = input("请输入您要增加的员工信息（格式要求 zengchuixin,22,12378902792,IT,2014-06-23）：").strip()
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

@staff_info(func_type='mod_type')
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
        # print(user_list) 结果是一个列表
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

@staff_info(func_type='del_type')
def delete():
    user_del = input("请输入您要删除的员工的ID：").strip()
    # 用户的ID必须是数字，如果用户输入的不是数字，则提示用户输入正确的ID
    if not user_del.isdigit():
        print("请输入正确的员工ID号：\n")
        return
    else:
        with open('staff_info.txt','r',encoding='utf-8') as f,\
            open('staff_info_new','w',encoding='utf-8') as f2:
            # 逐行读取原始员工信息表中的内容
            for line in f:
                user_info = line.strip().split(',')
                # 如果用户输入的数字和员工信息表元素0所在的数字匹配，则代表要删除的用户存在
                if user_del == user_info[0]:
                    # 提示用户已删除员工，并打印出来已删除的员工信息
                    print("已删除员工 %s" % line)
                    continue
                # 如果不满足iF的条件，则把不满足的所有行写入到新的文件，满足的不写入，实现删除效果
                # 问题：永远只能删一行
                # 问题解决：通过前面定义的装饰器解决，如果有staff_info_new文件，则删除原始的staff_info文件，然后把new
                # 文件重命名为staff_info.txt即可
                else:
                    if not line[0].isdigit():
                        f2.write(line.strip())
                    else:
                        f2.write('\n'+line.strip())

# 定义查询界面
while True:
    print("""1.模糊查询
    2.创建新员工
    3.修改员工信息
    4.删除员工信息
    5.退出
    """)
    menu_dict = {'1':search,'2':add,'3':modify,'4':delete}
    user_chosen = input("请输入您想要操作的选项序号：")
    if user_chosen in menu_dict.keys():
        # 执行用户选择的函数
        menu_dict[user_chosen]()
    elif user_chosen == '5':
        exit("下次再见！")
    else:
        print("请输入正确的格式！")