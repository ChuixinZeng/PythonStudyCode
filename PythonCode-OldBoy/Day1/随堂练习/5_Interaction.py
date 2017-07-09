# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# raw_input 2.x input 3.x
#input 2.x 里输出的结果必须是定义好的变量，不建议用，很多余的语法，忘记他，不要用它

#要求格式化输出为下面的格式

name = input("name:")
age = int(input("age:")) #强制数据类型转换，默认age是string，这里强制转换成int
#打印当前数据类型
print(type(age),type(str(age))) #把int再转换成string
job = input("job:")
salary = input("salary:")

#字符串拼接，+号拼接的方式效率比较低下

#info = '''
#-------- info of '''  + name + ''' -----
#Name:'''+ age +'''
#Age:'''+ job+'''
#Job:''' + job +'''
#Salary:''' + salary
#print(info)

#更简单的字符串拼接方法，使用%s占位符,是string的简写
#下面括号有两个name，第一个name代表info of 后面的%s
#info = '''
#------------- info of %s ---------
#Name:%s
#Age:%s
#Job:%s
#Salary:%s
#''' %(name,name,age,job,salary)

#print(info)

#上面的输出可以定义数据类型，d代表只能接受数据

info1 = '''
------------- info of %s ---------
Name:%s
Age:%d
Job:%s
Salary:%s
''' %(name,name,age,job,salary)

print(info1)

#官方建议用下面这个

info2 = '''
------------- info of {_name} ---------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
''' .format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)

print(info2)

#下面的也可以，但是参数显得不够清晰
#format只有上面和下面这两种格式

info3 =  '''
------------- info of {0} ---------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
''' .format(name,age,job,salary)

print(info3)


