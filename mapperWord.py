#!/usr/bin/env python
import sys
import csv
import math
import string
import nltk
from nltk import word_tokenize          
from nltk.stem.porter import PorterStemmer


csv.field_size_limit(sys.maxsize)
# input comes from STDIN (standard input)
stopwords=['.','!',';',',','\'',':','-','_','?','@','#','RT','http','https','(',')','me','like','1','2','3','4','5','6','7','8','9','0']
data = sys.stdin.readlines()
csvreader = csv.reader(data, delimiter='\t')
for row in csvreader:
	#Select category 
	# remove leading and trailing whitespace
	text = row[5].strip().decode('utf-8')
    	# split the line into words
	tokens = nltk.word_tokenize(text)
	text = [ch.lower() for ch in tokens if ch not in stopwords]
	# increase counters
	for word in text:
		# write the results to STDOUT (standard output);
		try:
        		print '%s\t%s\t%s' % (word,row[1], 1)
		except :
			continue
