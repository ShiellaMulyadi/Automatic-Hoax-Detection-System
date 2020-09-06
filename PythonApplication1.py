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

# read csv
with open('HoaxDetection-master/Data frame/Data Mentah/600 news with valid hoax label.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        with open('HoaxDetection-master/Data frame/600 news with valid hoax label-cased folding+remove stopword+stemming.csv', 'a+', newline='') as write_obj: 
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Casefold
            row[0] = row[0].casefold()
            # remove stopword + stemming
            sentence = row[0].split()
            removed = []
            for word in sentence:
                word = stemmer.stem(word)
                if word not in listStopword:
                    removed.append(word)
                else:
                    pass
            row[0] = removed
            # Add contents of list as last row in the csv file
            csv_writer.writerow(row)
            
                        