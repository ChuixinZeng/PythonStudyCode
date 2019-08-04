# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 示例一：面向过程的编程无法很好的区分要调用的函数或者对象

def person(name,age,sex,job):
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job
    }
    return data

def dog(name,dog_type):
    data = {
        'name':name,
        'dog_type':dog_type
    }
    return data

def bark(d):
    print("dog %s:wang.wang.wang...." %d['name'])

def walk(p):
    print("person %s is walking..." %p['name'])


d1 = dog("李磊", "京巴")
p1 = person("张三", 25, "F", "engineer")
p2 = person("李四", 26, "F", "IT")

# walk(p1)
# bark(d1)

# 执行结果：
'''
person 张三 is walking...
dog 李磊:wang.wang.wang....

'''
# 上面的方式弊端之一在于，可以把人的对象传给够的方法

# bark(p1) # 运行结果dog 张三:wang.wang.wang....

# 示例二：在代码级别限制人不能调用狗的功能

def person1(name,age,sex,job):
    def walk(pp):
        print("person %s is walking...." % pp[name])

    data = {

        'name':name,
        'age':age,
        'sex':sex,
        'job':job,
        'walk':walk
    }

    return  data

def dog1(name,dog_type):
    def bark(dd):
        print("dog %s:wang wang wang...." % dd['name'])

    data = {
        'name':name,
        'tye':dog_type,
        'bark':bark
    }
    return data

d2 = dog1("李磊", "京巴")
p3 = person1("张三", 25, "F", "engineer")
p4 = person1("李四", 26, "F", "IT")

d2['bark'](p3) # 但是仍然可以把人的对象传给狗的方法
walk(d2)
'''
刚才你只是阻止了两个完全 不同的角色 之前的功能混用， 但有没有可能 ，同一个种角色，但有些属性是不同的呢？ 比如 ，大家都打过cs吧，cs里有警察和恐怖份子，但因为都 是人， 所以你写一个角色叫 person(), 警察和恐怖份子都 可以 互相射击，但警察不可以杀人质，恐怖分子可以，这怎么实现呢？ 你想了说想，说，简单，只需要在杀人质的功能里加个判断，如果是警察，就不让杀不就ok了么。 没错， 这虽然 解决了杀人质的问题，但其实你会发现，警察和恐怖分子的区别还有很多，同时又有很多共性，如果 在每个区别处都 单独做判断，那得累死。 

你想了想说， 那就直接写2个角色吧， 反正 这么多区别， 我的哥， 不能写两个角色呀，因为他们还有很多共性 ， 写两个不同的角色，就代表 相同的功能 也要重写了
'''

# 面向过程与面向对象：如果只是写个脚本无所谓，但如果写一个特别复杂的程序，就不太适合面向过程了，耦合度太高
# 下面是面向过程语法结构的示例

def db_conn():
    print("connecting db...")


def db_backup(dbname):
    print("导出数据库...", dbname)
    print("将备份文件打包，移至相应目录...")


def db_backup_test():
    print("将备份文件导入测试库，看导入是否成功")


def main():
    db_conn()
    db_backup('my_db')
    db_backup_test()


if __name__ == '__main__':
    main()