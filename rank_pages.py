# Michelle Scheuer
# CS 432
# 10/19/2021

import numpy

# td-idf = td * idf
# (occurrence in doc / words in doc) * log2(total doc corpus/num doc with term)

term_frequency = [(3 / 22), (6 / 24), (11 / 30), (3 / 10),
                  (1 / 21), (6 / 17), (10 / 43), (2 / 12), (2 / 10), (1 / 4)]
search_results = 2450000000
google_corpus = 35000000000 # worldwidewebsize.com estimate for 10/19/2021
IDF = numpy.log2(google_corpus / search_results)

for TF in term_frequency:
   TF_IDF = TF * IDF

   print(round(TF_IDF, 3), round(TF, 3), round(IDF, 3))