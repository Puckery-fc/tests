# -*- coding: utf-8 -*-
# File  : wexcel.py
# Date  : 2018/9/20

import xlwt
#只能读不能写
datas = [['姓名', '年龄', '性别', '分数'],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9]
        ]
book = xlwt.Workbook() #新建一个excel
sheet = book.add_sheet("casel_sheet") #添加一个sheet页
row = 0 #控制行
for data in datas:
    col = 0 #控制列
    for s in data: #再循环里面list的值，每一列
        sheet.write(row,col,s)
        col += 1
        row += 1
        book.save("H:\\fc\\txt&excel的读写\\excel读写\\stu_1.xls") #保存文件的目录