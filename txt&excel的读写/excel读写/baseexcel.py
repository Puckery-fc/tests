# -*- coding: utf-8 -*-
# File  : baseexcel.py
# Date  : 2018/9/19

import xlrd
# 打开excel表格，参数是文件路径
data = xlrd.open_workbook("H:\\fc\\txt&excel的读写\\excel读写\\333.xlsx")
table = data.sheet_by_name("Sheet1")

# 获取一行或一列的值，参数是第几行
print(table.col_values(0))    # 获取第一行的值，返回列表
print(table.row_values(3))    # 获取第一列的值，返回列表
