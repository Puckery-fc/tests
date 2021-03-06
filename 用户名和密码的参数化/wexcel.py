# -*- coding: utf-8 -*-
# File  : wexcel.py
# Date  : 2018/9/12

import xlwt;
import xlrd;
# import xlutils;
from xlutils.copy import copy;

styleBoldRed = xlwt.easyxf('font: color-index red, bold on');
headerStyle = styleBoldRed;
wb = xlwt.Workbook();
ws = wb.add_sheet(gConst['xls']['sheetName']);
ws.write(0, 0, "Header", headerStyle);
ws.write(0, 1, "CatalogNumber", headerStyle);
ws.write(0, 2, "PartNumber", headerStyle);
wb.save(gConst['xls']['fileName']);

# open existed xls file
# newWb = xlutils.copy(gConst['xls']['fileName']);
# newWb = copy(gConst['xls']['fileName']);
oldWb = xlrd.open_workbook(gConst['xls']['fileName'], formatting_info = True);
printoldWb;  # <xlrd.book.Book object at 0x000000000315C940>
newWb = copy(oldWb);
printnewWb;  # <xlwt.Workbook.Workbook object at 0x000000000315F470>
newWs = newWb.get_sheet(0);
newWs.write(1, 0, "value1");
newWs.write(1, 1, "value2");
newWs.write(1, 2, "value3");
print("write new values ok");
newWb.save(gConst['xls']['fileName']);
print("save with same name ok");
