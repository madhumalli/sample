import json
json1 = json.loads(open('C:\\Users\\mmalli\\Desktop\\vscode\\convert_xlsx_to_jason\\CTEST 40K Test Files with Scores #1 08-2019_sheet1.json').read())


json2 = json.loads(open('C:\\Users\\mmalli\\Desktop\\vscode\\ex_jason.json').read())

print(len(json1['BORROWERS']))
print(len(json2))

final_one= { "mph_ho_id": "3333333333",
   "lenderLoanNbr": "1234567",
   "mi_trans_num": "1171535",
   "creditOverrideFlag": "",
   "ersEraVersion": "", 'BORROWERS':json1['BORROWERS'][1:9] , 'ERS_ERA_REQUESTS':json2 }

ex_j = json.dumps(final_one)

with open('C:\\Users\\mmalli\\Desktop\\vscode\\\python_scripts\\input_1sh_8_1.json', 'w') as f:
    f.write(ex_j)
    