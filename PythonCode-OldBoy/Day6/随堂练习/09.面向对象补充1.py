# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

'''

1、什么是面向对象编程？
    - 以前使用的是函数，现在是使用类和对象
2、什么是类，什么是对象，又有什么关系？
    - 类就是一个个函数的集合，模块里面包着类，类里面是函数
    - 有类之后，是通过对象去调用（obj = 类()），即先实例化；没有类的话是直接调用函数了

3、不会面向对象，也能实现功能，但是虽然函数编程能实现，但是比较麻烦。如果用面向对象就非常容易实现
4、JAVA和C#只支持面向对象编程，而Python可以用函数式编程，比如写脚本等
5、什么时候适用面向对象？
    - 公共的功能提取出来（参考 "图片04.面向对象补充"）,根据一个模板去创建多个对象
    - 多个函数需要传公共的参数（例如hostname、pwd）参考
        图片05.面向对象补充-函数式编程传参数弊端
        图片06.面向对象补充-函数式编程传参数弊端（解决）
6、self是什么？就是调用当前方法的对象

class foo:
    # 共有属性
    # 静态字段，如果中国有32个身份，每个里面都要写属于的国家，那么就用静态字段，只需要保存一份
    # 每个对象中保存相同的东西时，可以使用静态字段
    country = "中国"
    def __init__(self,name):
        # 普通字段
        # 普通属性
        self.NAME = name
        self.Count = count

    def bar(self):
        pass

obj1= foo('河南', 100000)
obj1.bar()

obj2 = foo('山东', 1000)
obj2.bar()
# obj1和obj2传给self

7、封装？
- 类中封装了字段和方法
- 对象中封装了：普通字段的值
- 封装除了能封装字符串，还能封装对象（下面例子）

class F1:
    def __init__(self,n);
        self.N =n
        print('F1')

class F2:
    def __init__(self,arg1);
        self.N =arg1
        print('F2')

class F3:
    def __init__(self,arg2);
        self.N =arg2
        print('F3')

o1 = F1('alex')
o2 = F2(o1)
o3 = F3(o2)

# 问题：怎么通过o3找到Alex？
o3.b.a.N = alex

8、继承？
参考图片07.继承示例

9、多态？多种形态，Python是弱类型语言，自带多态特性
10、
字段：
    普通字段（保存在对象中）
    静态字段（保存在类中）
方法：
    普通方法（保存在类中，调用者是对象，至少有一个self参数）
    静态方法（保存在类中，可以有任意个参数，对于静态方法，可以不创建对象，直接执行）
    class F1:
        @staticmethod
        def a1():
            print('alex')
    F1.a1() # 未创建对象，直接通过类调用静态方法，静态方法也是保存在类中

'''