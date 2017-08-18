# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import shutil
# 方法一：只拷贝文件
# f1 = open("本节笔记.txt",encoding="utf-8")
# f2 = open("笔记2","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)

# 方法二：只拷贝文件
# shutil.copyfile("笔记2","笔记3")

# 在源文件和目标文件都存在的情况下，将源文件的修改时间等状态信息拷贝到目标文件，目标文件的状态被替换掉
# 包括：mode bits,atime,mtime,flags，Windows上无法拷贝权限
shutil.copystat('笔记2','笔记3')

# shutil.copy() 拷贝文件和权限信息

# 拷贝目录：执行递归拷贝，即把拷贝的目录下面所有的子目录及文件全部拷贝到新的目录
# shutil.copytree('test3','test4')

# 删除目录
# shutil.rmtree('test4')

# 文件压缩打包，压缩的时候路径最好不要包含自己压缩包所在的路径，否则会多压缩一次
shutil.make_archive('笔记压缩','zip',root_dir=r'C:\Githubnew\PythonStudyCode\PythonCode-OldBoy\Day5\随堂练习\Shutil模块')

# shutil对压缩包的处理是调ZipFile和TarFile两个模块来进行的
import zipfile

# # 压缩
# z = zipfile.ZipFile('laxi.zip', 'w')
# z.write('a.log')
# z.write('data.data')
# z.close()
#
# # 解压
# z = zipfile.ZipFile('laxi.zip', 'r')
# z.extractall()
# z.close()

# tar包解压缩
import tarfile

# # 压缩
# tar = tarfile.open('your.tar','w')
# tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
# tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
# tar.close()
#
# # 解压
# tar = tarfile.open('your.tar','r')
# tar.extractall()  # 可设置解压地址
# tar.close()




