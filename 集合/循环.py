# -*- coding: utf-8 -*-
# File  : 循环.py
# Date  : 2018/11/8

# a,b = 0,1
# while b<10:
#     print(b)
#     a,b = b,a+b

'''
age = int(input("年龄:"))
print("")
if age <=0:
    print("false")
elif age == 1:
    print("true")
elif age == 2:
    print("true")
elif age >=2:
    human = 22 +(age-2)*5
    print("人的年龄：",human)
    input("enter")
'''

'''
num = int(input("输入的数字:"))
if num%3 == 0:
    if num%2 == 0:
      print("被3整除")
    else:
      print("被2整除")
else:
    if num%3 == 0:
      print("整除3")
    else:
      print("整除2")
'''

'''
#1到100的总和
n = 100
sum = 0
m = 1
while m<=100:
    sum = sum+m
    m += 1
print(sum)
'''

#无限循环
var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)

print("Good bye!")