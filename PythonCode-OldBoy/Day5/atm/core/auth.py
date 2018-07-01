#!_*_coding:utf-8_*_
import sys
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(base_dir)
sys.path.append(base_dir)

from core import db_handler
from bin import manage
from conf import settings
from core import logger
import json
import time



def login_required(func):
    "验证用户是否登录"

    def wrapper(*args,**kwargs):
        #print('--wrapper--->',args,kwargs)
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("用户还没有通过身份验证.")
    return wrapper


def acc_auth(account,password):
    '''
    用户认证函数
    :param account: 信用账户号码
    :param password: 信用账户密码
    :return: 如果通过身份验证，则返回账户对象，否则，返回None
    '''
    # settings就是conf里面的配置文件，目前默认是文件方式存储，这个地方把配置传进来
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path, account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() >exp_time_stamp:
                    print("\033[31;1m账户 [%s] 已经过期了,请与后台联系获取一张新卡!\033[0m" % account)
                else: # 通过身份验证
                    return  account_data
            else:
                print("\033[31;1m账户ID或者密码不正确!\033[0m")
    else:
        print("\033[31;1m账户 [%s] 不存在!\033[0m" % account)


def acc_auth2(account,password):
    '''
    优化版认证接口
    :param account: 信用账户号码
    :param password: 信用账户密码
    :return: 如果通过了身份验证，返回账户对象，如果没有通过，返回none

    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)
    if data["status"] == 2:  # 判断是否为管理者
        manage.manage_main(data)
    if data['status'] == 1:
        print("你的账户已经被冻结，请联系管理员！\n")
        option = input("请按b退出！")
        if option == "b":
            exit("程序已经退出！")

    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("\033[31;1m账户 [%s] 已过期,请联系后台开新卡!\033[0m" % account)
        else:  # 通过身份验证
            return data
    else:
        print("\033[31;1m账户ID或者密码不正确!\033[0m")

def acc_login(user_data,log_obj):
    '''
    账户登陆函数
    :user_data: 用户数据信息，仅仅放在内存里
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("\033[32;1m账户:\033[0m").strip()
        password = input("\033[32;1m密码:\033[0m").strip()
        # 程序的解耦，没有把身份验证方式写死
        auth = acc_auth2(account, password)
        if auth: # 如果不是none，代表通过了身份验证，登陆成功了，就去改全局的字典user_data
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            print("欢迎，认证成功！")
            return auth
        retry_count += 1
    else:
        log_obj.error("账户 [%s] 尝试了太多次登陆" % account)
        exit()
