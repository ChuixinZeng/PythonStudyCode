# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import sys

# 打印系统路径，可以看到是先从当前路径里面找的，所以在Python 2里面，起的py文件名称一定不能喝系统模块名称相同，
# 比如我的模块叫sys，那么py文件名不要起sys.py了
# ['E:\\GitRepository\\PythonStudyCode\\PythonCode-OldBoy\\Day2\\随堂练习', 'E:\\GitRepository\\PythonStudyCode\\PythonCode-OldBoy\\.idea',
# 'E:\\GitRepository\\PythonStudyCode\\PythonCode-OldBoy', 'C:\\Program Files\\Python36\\python36.zip', 'C:\\Program Files\\Python36\\DLLs',
# 'C:\\Program Files\\Python36\\lib', 'C:\\Program Files\\Python36', 'C:\\Program Files\\Python36\\lib\\site-packages']
# 系统有个环境变量，Python也有个全局的环境变量，上面的路径就是。python在导入库（比如sys模块）的时候，会从上面的目录去找

# python安装的的第三方库一般保存在'C:\\Program Files\\Python36\\lib\\site-packages'里面
# Python安装的标准库一般放在'C:\\Program Files\\Python36\\lib'里面

#print(sys.path)  #打印环境变量

print(sys.argv)# 在Python命令行里，打印的是当前脚本的名字相对路径；在pycharm里显示的是绝对路径，因为pycharm调用的时候写的就是绝对路径

# 打开CMD，切换到当前py所在的目录，执行下面的命令

'''
要查看的模块名是英文的话，可以正常显示
E:\GitRepository\PythonStudyCode\PythonCode-OldBoy\Day2\随堂练习>python sys_moudule.py
['sys_moudule.py']

E:\GitRepository\PythonStudyCode\PythonCode-OldBoy\Day2\随堂练习>python sys_moudule.py 1 2 3
['sys_moudule.py', '1', '2', '3']
如果要查看的模块名是中文，则乱码
E:\GitRepository\PythonStudyCode\PythonCode-OldBoy\Day2\随堂练习>python 模块初识.py
['\xc4\xa3\xbf\xe9\xb3\xf5\xca\xb6.py']
E:\GitRepository\PythonStudyCode\PythonCode-OldBoy\Day2\随堂练习>python 模块初识.py 1 2 3
['\xc4\xa3\xbf\xe9\xb3\xf5\xca\xb6.py', '1', '2', '3']

'''
# 取路径里面的2
# 下面定义好取2，然后在Python命令行直接输2就可以取到
print(sys.argv[2])

'''
上面定义好后，又多取到了一个值2
E:\GitRepository\PythonStudyCode\PythonCode-OldBoy\Day2\随堂练习>python sys_moudule.py 1 2 3
['sys_moudule.py', '1', '2', '3']
2
'''

# sys模块没找着，是因为sys是Python解释器自带的模块，没有放在目录里面
