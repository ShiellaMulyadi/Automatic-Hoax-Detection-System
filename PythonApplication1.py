#import basic library
#nltk.download()
import re
import string
import nltk 
#import for showing graphic
import matplotlib.pyplot as plt
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# impor word_tokenize dari modul nltk
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist
# import stopword removal 
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

#create stopword
factory2 = StopWordRemoverFactory()
stopword = factory2.create_stop_word_remover()

# stemming process
sentence = "Liputan6.com, California - Beberapa hari belakangan ini sejumlah keluhan pengguna iPhone 6 Plus meramaikan dunia maya. Smartphone anyar Apple berlayar 5,5 inci itu dilaporkan mudah melengkung bila terlalu lama disimpan di dalam saku celana. Sontak kabar ini menjadikan Apple bulan-bulanan di berbagai media sosial. Tak hanya para pengguna, beberapa kompetitor Apple pun tak menyia-nyiakan momen ini untuk 'menghajar' perusahaan berlogo buah apel tergigit itu."

cased_folding = sentence.strip().translate(str.maketrans("","",string.punctuation))
stopword = stopword.remove(cased_folding)
sentence_lower_cased = stopword.lower()
sentence_no_number = re.sub(r"\d+", "", sentence_lower_cased)
final_sentence = sentence_no_number
stemmed_sentence = stemmer.stem(final_sentence)
tokenized_sentences = nltk.tokenize.word_tokenize(stemmed_sentence)
kemunculan = nltk.FreqDist(tokenized_sentences)
#print(kemunculan.most_common())


print("\noriginal sentence")
print(sentence + "\n")
print("stopword sentence")
print(stopword+ "\n")
print("steemed sentence")
print(stemmed_sentence+ "\n")
print('tokenized sentence')
print(word_tokenize(stemmed_sentence))

#Showing Graphic kemunculuan
kemunculan.plot(30,cumulative=False)
plt.show()

