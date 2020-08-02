#import basic library
#nltk.download()
import re
import string
import nltk 
import csv
import pandas as pd
import numpy as np
#import for showing graphic
import matplotlib.pyplot as plt
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# impor word_tokenize dari modul nltk
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist
# import stopword removal 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# create stopword
listStopword =  set(stopwords.words('indonesian'))

# read csv
with open('testing1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:

        sentence = row[1]
        
        #cased folding process
        cased_folding = sentence.strip().translate(str.maketrans("","",string.punctuation))
        #lower case
        sentence_lower_cased = cased_folding.lower()
        #hapus angka
        sentence_no_number = re.sub(r"\d+", "", sentence_lower_cased)
        final_sentence = sentence_no_number
        stemmed_sentence = stemmer.stem(final_sentence)
        tokenized_sentences = nltk.tokenize.word_tokenize(stemmed_sentence)
        removed =[]
        for t in tokenized_sentences:
            if t not in listStopword:
                removed.append(t)
        #kemunculan = nltk.FreqDist(removed)
        #kemunculan.plot(30,cumulative=False)
        #plt.show()
        #print(kemunculan)
        """
        print("\noriginal sentence")
        print(sentence + "\n")
        print("steemed sentence")
        print(stemmed_sentence+ "\n")
        print('tokenized sentence')
        print(word_tokenize(stemmed_sentence))
        print('\nsentence after stopword removal')
        """
        print(removed)
 
