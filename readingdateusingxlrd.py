import xlrd
from datetime import date

wb = xlrd.open_workbook('C:\\Users\\mmalli\\Desktop\\MADU\\Videos_to_fix\\data_to_convert.xlsx')

sh = wb.sheet_by_index(0)
for rownum in range(1, sh.nrows):
    # for colnum in range(7,8):
    
    try:
        cellvalue = sh.cell_value(rowx = rownum, colx = 7)
        print(cellvalue)

        y, m, d, h, i, s = xlrd.xldate_as_tuple(cellvalue, wb.datemode)
        print(d,m,y)

        print("date: {0}/{1}/{2}".format(d, m, y))

    except:
        pass