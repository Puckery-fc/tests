# -*- coding: utf-8 -*-
# File  : 函数.py
# Date  : 2018/11/9

'''
def area(width,height):
    return width*height
x = 4
y = 5

print("width =", x, " height =", y, " area =", area(x, y))
'''

'''
#printme()
def printme(str):
    print(str)
    return
printme("打大")
printme("等等我")
'''

'''
#python传不可变对象实例
def ChangeInt(a):
  a = 10
b = 2
ChangeInt(b)
print(b)  # 结果是 2
'''
'''
#传可变对象实例
def changeme(mylist):
    #修改传入的列表
  mylist.append([1,2,3,4])
  print("函数内取值:",mylist)
  return
#调用changeme函数
mylist = [10,20,30]
changeme(mylist)
print("函数外取值:",mylist)
'''

'''
def printinfo(name,age):
    "打印任何传入的字符串"
    print("name:",name)
    print("age:",age)
    return
#调用printinfo函数
printinfo(name =" nnn",age = 555)
'''

#默认参数
def printinfo(name,age = 35)