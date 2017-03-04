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
data = sys.stdin.readlines()
csvreader = csv.reader(data, delimiter='\t')
#each record
for row in csvreader:
	# text
	text = row[5].strip().decode('utf-8')
	listText = text.split()
	# topic
	topic = row[0].strip().decode('utf-8')
	# category
	category = row[1].strip().decode('utf-8')
	# Retweet depth
	reDepth=0
	for word in listText:
		if word=="RT":
			reDepth+=1
	# Retweet ratio
	reRatio=0
	if "RT" in text:
		reRatio=1
	# Hashtag
	hashtags=row[6].strip()
	# Length
	length=len(text)
	# Exlamination
	exla=0
	if "!" in text:
		exla=1
	# Question
	quest=0
	if "?" in text:
		quest=1
	# Links
	link=row[7].strip()
	# Topic repetition
	topicRep=0
	topic = row[0].strip()
	for word in listText:
		if word.lower()==topic.lower():
			topicRep+=1
	
	# increase counters
	#print text row[4]=userid row[8]=1 if is retweeted else 0
	print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (topic,category,row[4],row[8],reDepth,reRatio,hashtags,length,exla,quest,link,topicRep)
	

