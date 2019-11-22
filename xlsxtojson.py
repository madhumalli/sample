import xlrd
from collections import OrderedDict
import os
from datetime import datetime
from datetime import date
import json

wb = xlrd.open_workbook('CTEST 40K Test Files with Scores #1 08-2019.xlsx')
sh = wb.sheet_by_index(3)

borrowers_list = []


for rownum in range(1, sh.nrows):
    
    borrower = OrderedDict()

    row_values = sh.row_values(rownum)

    # borrower['consumerid'] = row_values[0]
    # borrower['designatorCode'] = row_values[1]
    borrower['primary'] = 'N'
    
    for rownum in range(1,6):
        borrower['order'] = rownum
        

    borrower['firstName'] = row_values[0]
    
    borrower['lastName'] = row_values[2]
    borrower['middleName'] = row_values[1]
    borrower['suffix'] = row_values[3]
    try:
        borrower['ssn'] = str(int(row_values[4]))
        print(type(borrower['ssn']))
    except:
        pass
    # borrower['dateOfBirth'] = int(row_values[7])   
    # print('executed::',borrower['dateOfBirth'])
    # try:
    #     cellvalue = sh.cell_value(rowx = rownum, colx = 7)
    #     # print(cellvalue)
    #     print('executed:', cellvalue)

    #     y, m, d, h, i, s = xlrd.xldate_as_tuple(cellvalue, wb.datemode)
    #     # print(d,m,y)
    #     print('executed:', d,m,y)

    #     dob = ("{0}/{1}/{2}".format(d, m, y))
    #     print( dob)
    # except:
    #     pass
    # borrower['dateOfBirth'] = dob
    

    address={}
    address['street'] = row_values[5] + " " +row_values[6] + " " + row_values[7]
    address['city'] = row_values[8]
    address['state'] = row_values[9]
    try:
        address['postalCode'] = str(int(row_values[10]))
        print(type(address['postalCode']))
    except:
        pass


    borrower['ADDRESSES'] = [address]


    borrowers_list.append(borrower)
    
j = json.dumps({'BORROWERS':borrowers_list})

with open('CTEST 40K Test Files with Scores #1 08-2019_sheet3.json','w') as f:
    f.write(j)