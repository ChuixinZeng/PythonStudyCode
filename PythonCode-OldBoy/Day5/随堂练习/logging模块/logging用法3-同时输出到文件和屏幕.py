# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# Python 使用logging模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：
#
# 1. logger提供了应用程序可以直接使用的接口；
#
# 2. handler将(logger创建的)日志记录发送到合适的目的输出；
#
# 3. filter提供了细度设备来决定输出哪条日志记录；
#
# 4. formatter决定日志记录的最终输出格式。

import logging

# create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
# 输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
# 输出到文件，加上encoding可以防止中文乱码
fh = logging.FileHandler("access.log",encoding="utf-8")
fh.setLevel(logging.WARNING)
# create formatter
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
# 可以为不同的输出（屏幕或文件）设置不同的foramt格式
ch.setFormatter(formatter1)
fh.setFormatter(formatter2)

# add ch and fh to logger
# 格式设置完成后，需要告诉logger往上面两个方式进行输出
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

'''
logger
每个程序在输出信息之前都要获得一个Logger。Logger通常对应了程序的模块名，比如聊天工具的图形界面模块可以这样获得它的Logger：
LOG=logging.getLogger(”chat.gui”)
而核心模块可以这样：
LOG=logging.getLogger(”chat.kernel”)

Logger.setLevel(lel):指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
Logger.addFilter(filt)、Logger.removeFilter(filt):添加或删除指定的filter
Logger.addHandler(hdlr)、Logger.removeHandler(hdlr)：增加或删除指定的handler
Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()：可以设置的日志级别

 

handler

handler对象负责发送相关的信息到指定目的地。Python的日志系统有多种Handler可以使用。有些Handler可以把信息输出到控制台，有些Logger可以把信息输出到文件，还有些 Handler可以把信息发送到网络上。如果觉得不够用，还可以编写自己的Handler。可以通过addHandler()方法添加多个多handler
Handler.setLevel(lel):指定被处理的信息级别，低于lel级别的信息将被忽略
Handler.setFormatter()：给这个handler选择一个格式
Handler.addFilter(filt)、Handler.removeFilter(filt)：新增或删除一个filter对象


每个Logger可以附加多个Handler。接下来我们就来介绍一些常用的Handler：
1) logging.StreamHandler
使用这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息。它的构造函数是：
StreamHandler([strm])
其中strm参数是一个文件对象。默认是sys.stderr


2) logging.FileHandler
和StreamHandler类似，用于向一个文件输出日志信息。不过FileHandler会帮你打开这个文件。它的构造函数是：
FileHandler(filename[,mode])
filename是文件名，必须指定一个文件名。
mode是文件的打开方式。参见Python内置函数open()的用法。默认是’a'，即添加到文件末尾。

3) logging.handlers.RotatingFileHandler
这个Handler类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建 一个新的同名日志文件继续输出。比如日志文件是chat.log。当chat.log达到指定的大小之后，RotatingFileHandler自动把 文件改名为chat.log.1。不过，如果chat.log.1已经存在，会先把chat.log.1重命名为chat.log.2。。。最后重新创建 chat.log，继续输出日志信息。它的构造函数是：
RotatingFileHandler( filename[, mode[, maxBytes[, backupCount]]])
其中filename和mode两个参数和FileHandler一样。
maxBytes用于指定日志文件的最大文件大小。如果maxBytes为0，意味着日志文件可以无限大，这时上面描述的重命名过程就不会发生。
backupCount用于指定保留的备份文件的个数。比如，如果指定为2，当上面描述的重命名过程发生时，原有的chat.log.2并不会被更名，而是被删除。


4) logging.handlers.TimedRotatingFileHandler
这个Handler和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就 自动创建新的日志文件。重命名的过程与RotatingFileHandler类似，不过新的文件不是附加数字，而是当前时间。它的构造函数是：
TimedRotatingFileHandler( filename [,when [,interval [,backupCount]]])
其中filename参数和backupCount参数和RotatingFileHandler具有相同的意义。
interval是时间间隔。
when参数是一个字符串。表示时间间隔的单位，不区分大小写。它有以下取值：
S 秒
M 分
H 小时
D 天
W 每星期（interval==0时代表星期一）
midnight 每天凌晨
'''