# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import sys
import readline
import rlcompleter

if sys.platform == 'darwin' and sys.version_info[0] == 2:
     readline.parse_and_bind("bind ^I rl_complete")
else:
     readline.parse_and_bind("tab: complete")  # linux and python3 on mac

     '''
     用法

     localhost:~ jieli$ python
     Python 2.7.10 (default, Oct 23 2015, 18:05:06)
     [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
     Type "help", "copyright", "credits" or "license" for more information.
     >>> import tab

     '''