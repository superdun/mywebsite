# -*- coding: utf-8 -*-
import xlrd
import xlwt
def write(dict):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('123')
    for i in range(len(dict.keys())):
        ws.write( i, 0,dict.keys()[i])
        ws.write(i, 1,dict.values()[i])
    wb.save(u'C:\\Users\\lidad\\Desktop\\resultChild2.xls')
def write2(dict):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('123')
    for i in range(len(dict.keys())):
        ws.write(i, 0, dict.keys()[i])
        for j in range(len(dict.values()[i])):

            ws.write(i, 1+j,dict.values()[i][j])
    wb.save(u'C:\\Users\\lidad\\Desktop\\resultChild2.xls')
book1 = xlrd.open_workbook(u'C:\\Users\\lidad\\Desktop\\missingchild.xls')
sh1 = book1.sheet_by_name('Sheet1')
ages={}
# for i in range(sh1.nrows):
#     try:
#         age = int(sh1.row_values(i)[7][:4]) - int(sh1.row_values(i)[5][:4])
#         gender = sh1.row_values(i)[4]
#         # age =  (1+(int(sh1.row_values(i)[8][:4])-int(sh1.row_values(i)[5][:4]))/5)*5
#         if age in ages.keys():
#             if gender==u'男':
#                 ages[age][0] += 1
#             else:
#                 ages[age][1]+= 1
#         else:
#             if gender==u'男':
#                 ages[age] = [1,0]
#             else:
#                 ages[age] = [0, 1]
#     except UnicodeEncodeError or ValueError:
#         pass
provinces = {}
for i in range(sh1.nrows):
    try:
        gender = sh1.row_values(i)[4]
        province = sh1.row_values(i)[14][:2]
        # age =  (1+(int(sh1.row_values(i)[8][:4])-int(sh1.row_values(i)[5][:4]))/5)*5
        if province in provinces.keys():
            if gender==u'男':
                provinces[province][0] += 1
            else:
                provinces[province][1]+= 1
        else:
            if gender==u'男':
                provinces[province] = [1,0]
            else:
                provinces[province] = [0, 1]
    except UnicodeEncodeError or ValueError:
        pass

write2(provinces)