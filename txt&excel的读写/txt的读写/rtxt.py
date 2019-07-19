# -*- coding: utf-8 -*-
# File  : rtxt.py
# Date  : 2018/9/12
fname = input("Enter filename:")  # 读取字符，与C++中的cin>>类似
try:    # try...expect是python中的异常处理语句，try中写
    fobj=open(fname,"r")  # 待检测的操作语句
except IOError:         # expect中写差错处理语句
    print("file open error:")
else:                   # else中处理正常情况
    for eachLine in fobj:
        print(eachLine)
        fobj.close()
        input("press enter to close")