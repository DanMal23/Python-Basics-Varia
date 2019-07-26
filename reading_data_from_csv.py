#!/usr/bin/env python
# coding: utf-8


# min, max, - at line number and value of salination at value of min or max of herring's length
import csv
with open('/home/d/Documents/workspaces/files/herrings.csv', 'r') as f:
    reader = csv.reader(f)
    values=[]
    next(reader)           
    for col in reader:
        line_num = col[0]
        herr_length = float(col[1])
        water_salination ='{:.2f}'.format(float(col[13]))
        values.append({"line number" : line_num, "val len" : herr_length, "wat sal" : water_salination})  
maxL = max([value["val len"] for value in values])
minL  = min([value["val len"] for value in values])
averL = '{:.2f}'.format(sum([value["val len"] for value in values]) /len(values))
print("Average length of herrings: ", averL)
for value in values:
    if value["val len"] == maxL:
        print("Max == {}, at salination:{}, data in line: {}".format(value["val len"],value["wat sal"],value["line number"]))
    if value["val len"] == minL:
        print("Min == {}, at salination:{}, data in line: {}".format(value["val len"],value["wat sal"],value["line number"]))
#output:
#Average length of herrings:  25.30
#Max == 32.5, at salination:35.51, in line: 11858
#Max == 32.5, at salination:35.51, in line: 19722
#Min == 19.0, at salination:35.40, in line: 44316
#Min == 19.0, at salination:35.61, in line: 44776

print("-----------------------------------------------------")

# number of columns,rows, names of comumns
import csv
with open('/home/danuta/Documents/workspaces/files/herrings.csv', 'r') as f:
    reader = csv.reader(f)
    # columns
    column_num = len(header) #num of columns
    print("Number of columns: ", column_num)
    #rows
    values=[]
    row_count = 0
    for row in reader:
        if row_count == 0:
            print(f'Column names: {", ".join(row)}')       
            row_count += 1
        else:
            row_count +=1
    print(f'Number of rows: {row_count} ')
#output:
#Number of columns:  16
#Column names: , length, cfin1, cfin2, chel1, chel2, lcop1, lcop2, fbar, recr, cumf, totaln, sst, sal, xmonth, nao
#Number of rows: 52583 

print("-----------------------------------------------------")

# min/max 'total yearly catch in a region, col [10]-'cumf'
import csv
with open('/home/d/Documents/workspaces/files/herrings.csv', 'r') as f:
    reader = csv.reader(f)
    values=[]
    next(reader)
    for col in reader:
        row_num = col[0]
        herr_num = float(col[9])
        fishing_rate = float(col[10])
        herr_total = '{:.4f}'.format(float(col[11]))
        values.append({"row num" : row_num, 
                       "herr num" : herr_num, "fish rate" : fishing_rate, "herr tot" : herr_total})
maxNum = max([value['fish rate'] for value in values])
minNum = min([value['fish rate'] for value in values])
averN = sum([value['fish rate'] for value in values]) /len(values)

print("AVERAGE fish rate: ", '{:.3f}'.format(averN))
for value in values:
    if value['fish rate'] == maxNum:
        print('MAX: {}, at herr num: {}, with total caught: {} - line: {}'
              .format(value['fish rate'], value['herr num'], value['herr tot'], value['row num']))
    if value['fish rate'] == minNum:
        print('MIN: {}, at herr num: {}, with total caught: {} - line: {}'
              .format(value['fish rate'], value['herr num'], value['herr tot'], value['row num']))
              
print("-----------------------------------------------------")

# enumerating headers:
import csv
with open('/home/d/Documents/workspaces/files/herrings.csv', 'r') as f:
    reader = csv.reader(f)  
    i = next(reader)
    print(list(enumerate(i)))
#output:
#[(0, ''), (1, 'length'), (2, 'cfin1'), (3, 'cfin2'), (4, 'chel1'), (5, 'chel2'), (6, 'lcop1'), (7, 'lcop2'), (8, 'fbar'), (9, 'recr'), (10, 'cumf'), (11, 'totaln'), (12, 'sst'), (13, 'sal'), (14, 'xmonth'), (15, 'nao')]

print("-----------------------------------------------------")

# enumerating headers with DictReader:
import csv
with open('/home/d/Documents/workspaces/files/herrings.csv', 'r') as f:
    reader = csv.DictReader(f)    
    headers = reader.fieldnames
    list_headers = list(enumerate(headers))
    print(*list_headers)




