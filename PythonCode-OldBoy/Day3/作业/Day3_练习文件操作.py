# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入正则表达式、时间日期模块
import re,datetime

# 定义ha_config变量，内容是ha_config.conf文件
ha_config = "ha_config.conf"
# 定义时间日期变量，供后面备份文件时使用
bk_flag = datetime.datetime.now().strftime("%Y%H%M%S")

# 定义update_file函数，该函数包含两个参数f1和f2，用于更新文件内容
# 作用：用于删除backend，原理是，如果在ha_config中匹配到要删除的backend文件的话，不处理，不匹配的内容全部写入到ha_config.bk
# 这样结束循环后，把ha_config.bk的内容写回到ha_config，那些匹配的内容自然就删掉了。。。
def update_file(f1,f2):
    # 以写方式打开文件f1，以读方式打开文件f2
    # 下面这种with as写法的好处是不需要再使用close关闭文件了
    # f代表f1,f_old代表f2
    # 目的是把f2的内容更新到f1中
    with open(f1,"w") as f,open(f2,"r") as f_old:
        f.write(f_old.read())
        # flush操作执行后，才会把数据真正写入到f1对应的文件里面
        f.flush()

# 定义一个backup_file的函数，该函数包含一个参数f，用于将原始文件备份
def backup_file(f):
    # 定义f_bk变量，用于写打开.bk备份文件，文件名由f参数指定的名称+bk_flag定义的时间组成
    f_bk = open("%s_%s.bk" %(f,bk_flag),"w")
    # 这里f的文件名实际上原始文件和备份文件是一样的，只不过备份文件名多了一个日期
    # 所以，备份文件名是f+bk_flag，而原始文件名是f
    with open(f,"r",encoding="utf-8") as f:
        # 将原始文件内容备份到bk备份文件中
        f_bk.write(f.read())
        f_bk.flush()

# 定义update函数，进行haconfig.conf文件的更新
def update(args):
    if args:
        # 调用backup_file函数，针对原始的ha_config进行备份，备份完成的文件名是带日期的
        backup_file(ha_config)
        # 备份完成后，再执行下面的update操作
        # 以读打开ha_config文件，以写模式打开ha_config.bak文件，如果没有就新建
        with open(ha_config,"r") as f,open("%s.bk"% ha_config,"w") as f_new:
            # 从原始的ha_config文件循环读取内容，按行读取
            for line in f:
                # 利用正则表达式匹配每一行，如果能匹配用户输入的server info中的backend和record的话执行if进行更新
                # 不匹配的每一行都执行else
                if re.match(args["backend"],line):
                    # 更新backend行的值
                    f_new.write(line)
                    # 更新record行的值，\t是制表符
                    f_new.write("\t%s" % args["record"])
                    line = f.readline() # 继续读取下一行，直到循环结束
                else:
                    # 如果正则表达式没有匹配到backend字典的值,则将ha_config的值逐行写入到ha_config.bk中
                    f_new.write(line)
        # ，最终update完成的信息会放在bk文件里，然后调用更新文件的函数，将更新完成的ha_config.bk文件内容写回到ha_config
        update_file(ha_config,"%s.bk" % ha_config)

# 定义一个函数，用于往ha_config文件里面新增backend内容
def add_new_backend(args):
    if args:
        # 操作前先备份文件，备份完成的文件名是带日期的
        backup_file(ha_config)
        # 利用追加模式打开ha_config文件，也就是说文件如果不存在则创建；存在则只追加内容
        fp = open(ha_config,"a")
        # 追加的内容就是backend和record的值
        fp.write("\n%s\n\t%s" % (args["backend"],args["record"]))
        # 最佳写入完成后，关闭文件
        fp.close()

# 定义一个函数，用户判断特定backend和record的值是不是存在
def config_diff(backend,record):
    # 2代表backend和record都已存在，1代表backend已存在,但是record值不一样，0代表backend不存在
    # 以读模式打开ha_config文件
    fp =open(ha_config,"r")
    # 设置result的值为0
    result = 0
    # 从ha_config文件里面读取内容
    for line in fp:
        # 如果读到了包含backend的行
        if re.match(backend,line):
            # 则返回值1
            result = 1
            # 继续读取下一行
            line = fp.readline()
            # 如果读到了包含record的行
            if re.match(".*%s" % record,line):
                #则告诉用户已经发现匹配的文件
                print("The backend config is found!")
                # 返回值为2
                result = 2
                # 中断循环
                break
    return result # 函数的返回值为result的具体值

# 定义一个函数，用于添加或者更新ha_config.conf中的backend
def add(args):
    # backend_info的值来源于函数convert_dict_to_conf，这个函数是把字典的值转换成配置文件
    backend_info = convert_dict_to_conf(args)
    if backend_info:
        # 调用config_diff函数，将backend_info中的值和ha_config中的值进行对比，以方便判断是否要添加新的backend或者更新backend
        diff = config_diff(backend_info["backend"],backend_info["record"])
        # 如果config_diff函数的返回值是2，则代表已经存在backend下面的record的值
        if diff == 2:
            print("The backend is already exists!")
        # 如果config_diff的函数的返回值是1，则代表匹配backend行的值，但是不匹配record的值，代表record的值有更新
        # 这种情况下就不是添加新的backend，而是更新现有的backend信息
        elif diff == 1:
            update(backend_info)
        # 如果以上条件都不满足，代表需要往ha_config中增加内容
        else:
            # 调用add_new_backend函数，增加新的内容
            add_new_backend(backend_info)
    else:
        return 0

# 定义一个函数，用于删除ha_config中的backend行
def delete_backend(args):
    if args:
        # 操作之前先备份
        backup_file(ha_config)
        # 以读模式打开ha_config，以写模式打开ha_config.bk
        with open(ha_config,"r") as f,open("%s.bk" % ha_config,"w") as f_new:
            # 循环遍历ha_config中的每一行
            for line in f:
                # 如果有匹配backend的行
                if re.match(args["backend"],line):
                    # 将读取到的值放到Line中
                    line = f.readline()
                else:
                    #如果没有匹配到，则更新ha_config.bk文件
                    f_new.write(line)
        # 调用update_file函数，将ha_config.bk文件更新到ha_config，这样就达到了删除匹配的行的目的
        update_file(ha_config,"%s.bk" % ha_config)

# 定义一个函数，用于删除backend
def delete(args):
    backend_info = convert_dict_to_conf(args)
    # 调用config_diff函数，将backend_info中的值和ha_config中的值进行对比，以方便判断要删除的值是否在ha_config.conf中
    if backend_info:
        diff = config_diff(backend_info["backend"],backend_info["record"])
        # 如果函数返回值是2，代表存在要删除的值
        if diff ==2:
            # 调用delete_backend进行删除操作
            delete_backend(backend_info)
        else:
            # 如果对比后，要删除的值不存在，则告诉用户值不存在
            print("not found")
            print(backend_info["backend"],backend_info["record"])
    else:
        return 0

# 定义一个函数search，用于查询用户输入的值是否存在
def search(args):
    # 以读方式打开ha_config文件
    fp = open(ha_config,"r")
    for line in fp:
        # 如果匹配到了用户输入的内容
        if re.match("backend %s" % args.strip(), line):
            # 则打印该行
            print(line.strip())
            # 读取下一行，即backend包含的record是什么
            print(fp.readline())
            break
    else:
        # 如果没有匹配的内容，则输入下面的信息
        print("not found '%s' in config file" % args.strip())

# 定义一个函数convert_to_dict，将用户输入的字符串类型转换成字典类型
def convert_to_dict(args):
    # 通过使用eval函数，可以把list,tuple,dict和string相互转化
    args = eval(args)
    # 如果args的内容是字典类型，则返回args
    if type(args) == type({}):
        return args
    else:
        # 如果不是字典类型，则返回空数组
        return ""

# 定义函数convert_dict_to_conf，用于将字典的内容转换成配置文件的格式
def convert_dict_to_conf(args):
    # 将字典转换成配置文件所使用的格式
    # 判断convert_to_dict函数的返回值args里面的keys是否包含backend和record
    if "backend" in args.keys() and "record" in args.keys():
        # 如果存在，则将backend和record的key对应的value转换为下面的格式
        backend = "backend %s" % (args["backend"].strip())
        record = "server %s weight %s maxconn %s" % (args['record']["server"],
                                                     args['record']["weight"], args['record']["maxconn"],)
        # 函数返回转换后的格式
        return {"backend":backend,"record":record}
    else:
        # 如果匹配键key失败，则输出错误信息
        print("格式错误，key:record 或者record错误")


def get_input_info():
    # 打印server info文字信息
    print("server info:")
    # 定义一个空字符串，用于保存用户输入的server info信息，即backend信息
    str_t = ""
    # iter函数，迭代器用起来很灵巧，你可以迭代不是序列但表现处序列行为的对象，例如字典的键、一个文件的行，等等
    for line in iter(input,""):
        # 将iter函数中用户输入的backend信息循环添加并追加到str_t变量中
        str_t += line
    # 将str_t变量的字符串值通过函数convert_to_dict转换为字典
    args = convert_to_dict(str_t)
    # 函数返回字典args的值，即server info下面用户输入的值
    if args:
        return args
    else:
        print("格式错误")

while True:
    # 交互式提示用户要做哪方面的查询
    choose = input("what are you want to do?(add/delete/search/q):")
    # 如果用户输入了search
    if choose == "search":
        # 则进一步提示用户输入要查询的backendname，并告诉用户输入的格式
        args = input("输入backend 域名进行查找（如：www.oldboy.org):")
        # 如果输入的信息正确
        if args:
            # 则调用search函数，进行查找，输出用户查找的内容
            search(args)
        # 如果输入的信息不正确，提示格式错误
        else:
            print("格式错误")
    # 如果用户输入的是q。则退出程序
    elif choose == "q":
        break
    # 如果用户输入的是add
    elif choose == "add":
        print(input("请输入完整的backend和record信息进行添加或者在域名和IP不变的情况下，输入新的weight和maxconn值进行更新，格式如下：\n"
                    "请按键盘enter键继续，在server info中输入完整的新的backend信息...."))
        # 则调用get_input_info函数，提示用户输入要添加的server info信息，并把添加的信息放到args中
        args = get_input_info()
        # 如果用户输入的信息没问题，则调用add函数，将用户提供的信息添加到ha_config文件中
        if args:
            add(args)
    # 如果用户输入的是delete
    elif choose == "delete":
        # 则调用get_input_info函数，提示用户输入要添加的server info信息，并把添加的信息放到args中
        args = get_input_info()
        # 如果用户输入的信息没问题，则调用delete函数，将用户提供的信息添加到ha_config文件中
        if args:
            delete(args)


