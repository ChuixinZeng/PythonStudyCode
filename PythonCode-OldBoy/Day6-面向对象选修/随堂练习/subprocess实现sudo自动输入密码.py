# -*- coding:utf-8 -*-

# Author:Chuixin Zeng


# subprocess实现sudo自动输入密码（Linux环境下测试）

def mypass():
    mypass = '123'  # or get the password from anywhere
    return mypass


echo = subprocess.Popen(['echo', mypass()],
                        stdout=subprocess.PIPE,
                        )

sudo = subprocess.Popen(['sudo', '-S', 'iptables', '-L'],
                        stdin=echo.stdout,
                        stdout=subprocess.PIPE,
                        )

end_of_pipe = sudo.stdout

print("Password ok \n Iptables Chains %s" % end_of_pipe.read())