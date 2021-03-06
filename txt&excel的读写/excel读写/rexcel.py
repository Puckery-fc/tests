# -*- coding: utf-8 -*-
# File  : rexcel.py
# Date  : 2018/9/19
import xlrd
class du:
    def __init__(self,excel_path,sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                    r.append(s)
                    j += 1
                    return  r
if __name__ == "__main__":
    filePath = "H:\\fc\\txt&excel的读写\\excel读写\\333.xlsx"
    sheetName = "Sheet1"
    data = du(filePath,sheetName)
    print(data.dict_data())