# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import subprocess


def Callps1():
    powerShellPath = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'
    powerShellCmd = "C:\PowerShellSample.ps1"

    p = subprocess.Popen([powerShellPath, '-ExecutionPolicy', 'Unrestricted', powerShellCmd, 'HELLO', 'WORLD']
                         , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    rc = p.returncode
    print("Return code given to Python script is: " + str(rc))
    print("\n\nstdout:\n\n" + str(output))
    print("\n\nstderr: " + str(error))

# Test
Callps1()

'''

C:\PowerShellSample.ps1

param(
    [string]$arg1,
    [string]$arg2
)
 
Write-Output $arg1
Write-Output $arg2
Output
stdout:
HELLO
WORLD
stderr: 
>>>

'''