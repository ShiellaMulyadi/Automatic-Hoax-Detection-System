#import basic library
#nltk.download()
import re
import string
import nltk 
import csv
import pandas as pd
from csv import writer
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stopword
listStopword =  set(stopwords.words('indonesian'))
# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()
dictionaryH = {}
dictionaryV = {}
TOTV = 0
TOTH = 0

#count words
def count(elements,label): 
    # if there exists a key as "elements" then simply 
    # increase its value. 
    if label =='Valid':
        if elements in dictionaryV: 
            dictionaryV[elements] += 1
        # if the dictionary does not have the key as "elements"  
        # then create a key "elements" and assign its value to 1. 
        else: 
            dictionaryV.update({elements: 1}) 
    else:
        if elements in dictionaryH: 
            dictionaryH[elements] += 1
        else: 
            dictionaryH.update({elements: 1}) 

# read csv
with open('Data frame/50 news with valid hoax label.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        with open('Data frame/5 news with valid hoax label-cased folding+remove stopword+stemming.csv', 'a+', newline='') as write_obj: 
        # Create a writer object from csv module   
           # Casefold
            xrow = row[0].translate(str.maketrans("","", string.punctuation)).casefold()
            sentence = stemmer.stem(xrow)
            tokenized_sentences = nltk.tokenize.word_tokenize(sentence)
            for t in tokenized_sentences:
                if t not in listStopword:
                    count(t,row[1]) 
                    if row[1] =="Valid":
                        TOTV+=1
                    else:
                        TOTH+=1
   
for allKeys in dictionaryV: 
    if allKeys in dictionaryH.keys():   
        with open('Data frame/final.csv', 'a+', newline='') as write_obj:
            writer = csv.writer(write_obj)
            writer.writerow([allKeys,
            dictionaryV[allKeys]/TOTV,
            dictionaryH[allKeys]/TOTH,
            (dictionaryV[allKeys]+dictionaryH[allKeys])/(TOTH+TOTV),
            TOTV/(TOTH+TOTV),
            TOTH/(TOTH+TOTV),
            ((dictionaryV[allKeys]/TOTV)*((dictionaryV[allKeys]+dictionaryH[allKeys])/(TOTH+TOTV))/(TOTV/(TOTH+TOTV))),
            ((dictionaryH[allKeys]/TOTH)*((dictionaryV[allKeys]+dictionaryH[allKeys])/(TOTH+TOTV))/(TOTH/(TOTH+TOTV)))
            ])
    else :
        with open('Data frame/final.csv', 'a+', newline='') as write_obj:
            writer = csv.writer(write_obj)
            writer.writerow([allKeys,
            dictionaryV[allKeys]/TOTV,
            0,
            (dictionaryV[allKeys])/(TOTH+TOTV),
            TOTV/(TOTH+TOTV),
            TOTH/(TOTH+TOTV),
            ((dictionaryV[allKeys]/TOTV)*((dictionaryV[allKeys])/(TOTH+TOTV))/(TOTV/(TOTH+TOTV))),
            0
            ])
for allKeys in dictionaryH: 
    if allKeys not in dictionaryV.keys():
        with open('Data frame/final.csv', 'a+', newline='') as write_obj:
            writer = csv.writer(write_obj)
            writer.writerow([allKeys,
            0,
            dictionaryH[allKeys]/TOTH,
            (dictionaryH[allKeys])/(TOTH+TOTV),
            TOTV/(TOTH+TOTV),
            TOTH/(TOTH+TOTV),
            0,
            ((dictionaryH[allKeys]/TOTH)*((dictionaryH[allKeys])/(TOTH+TOTV))/(TOTH/(TOTH+TOTV)))
            ])
    else:
        pass

