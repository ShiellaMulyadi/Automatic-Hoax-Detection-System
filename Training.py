import string
import csv
import pandas as pd
from csv import writer
from decimal import Decimal

dictionaryH = {}
dictionaryV = {}
final = {}
TOTV = 0
TOTH = 0

#count words
def count(elements,label): 
    if label =='Valid':
        if elements in dictionaryV: 
            dictionaryV[elements] += 1
        else: 
            dictionaryV.update({elements: 1}) 
    elif label == 'Hoax':
        if elements in dictionaryH: 
            dictionaryH[elements] += 1
        else: 
            dictionaryH.update({elements: 1}) 
    else:
        pass

#training
with open('Data frame/5 news with valid hoax label.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        cased_folding = row[0].strip().translate(str.maketrans("","",string.punctuation))
        sentence = cased_folding.split()
        for i in sentence:
            count(str(i),row[1]) 
            if row[1] == "Valid":
                TOTV+=1
            elif row[1] == "Hoax":
                TOTH+=1
            else:
                pass
 
for allKeys in dictionaryV: 
    if allKeys in dictionaryH.keys():   
        final[allKeys] = [dictionaryV[allKeys]/TOTV,dictionaryH[allKeys]/TOTH,(dictionaryV[allKeys]+dictionaryH[allKeys])/(TOTH+TOTV)]
    else :
        final[allKeys] = [dictionaryV[allKeys]/TOTV,0/TOTH,(dictionaryV[allKeys])/(TOTH+TOTV)]
for allKeys in dictionaryH: 
    if allKeys not in dictionaryV.keys():
        final[allKeys] = [0/TOTV,dictionaryH[allKeys]/TOTH,(dictionaryH[allKeys])/(TOTH+TOTV)]
    else:
        pass

#testing
with open('Data frame/5 news with valid hoax label.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        cased_folding = row[0].strip().translate(str.maketrans("","",string.punctuation))
        sentence = cased_folding.split()
        valid = 1
        hoax = 1
        result = ''
        for i in sentence:
            for row in final:
                if i == row:
                    if final[row][0] > 0:
                        valid *= Decimal(final[row][0])
                    else:
                        pass
                    if final[row][1] > 0:
                        hoax *= Decimal(final[row][1])
                    else:
                        pass
                else:
                    pass

        if Decimal(valid) > Decimal(hoax):
            result = 'valid'
        elif Decimal(hoax) > Decimal(valid): 
            result = 'hoax'
        else:
            pass
        print (result)

