import xlrd
from collections import OrderedDict
import os
from datetime import datetime

wb = xlrd.open_workbook('C:\\Users\\mmalli\\Desktop\\MADU\\Videos_to_fix\\data_to_convert.xlsx')
sh = wb.sheet_by_index(0)

borrowers_list = []


for rownum in range(1, sh.nrows):
    
    borrower = OrderedDict()

    row_values = sh.row_values(rownum)

    borrower['consumerid'] = row_values[0]
    borrower['designatorCode'] = row_values[1]
    borrower['firstName'] = row_values[2]
    borrower['middleName'] = row_values[3]
    borrower['lastName'] = row_values[4]
    borrower['suffix'] = row_values[5]
    borrower['ssn'] = row_values[6]
    borrower['dateOfBirth'] = row_values[7]    

    address={}
    address['street'] = row_values[9] + row_values[10] + row_values[11]
    address['city'] = row_values[12]
    address['state'] = row_values[13]
    address['zipcode'] = row_values[14]


    borrower['ADDRESS'] = address


    borrowers_list.append(borrower)
    
j = json.dumps({'BORROWERS':borrowers_list})

with open('data1.json','w') as f:
    f.write(j)

    