#!/usr/bin/env python

from operator import itemgetter
import sys
import math

current_topic = None
current_count = 0
total_tweets=0
aver_depth=aver_ratio=aver_hastags=aver_length=aver_exla=aver_quest=aver_link=aver_topicRep=0
word = None
Dictionary_users = {}
Dictionary_retweeted = {}
Dictionary_hashtags = {}
Dictionary_words = {}
Dictionary_lang = {}
users_total=0
users_diver=1
retweeted_total=0
retweeted_diver=1
hashtags_total=0
hashtags_diver=1
lang_total=0
lang_diver=1
words_total=0
words_diver=1
text=[]
exlude=['\"','\'','[',']',' ','@',':','_','-']
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    topic,cat,lang,text,user,retweeted,reDepth,reRatio,hashtags,length,exla,quest,link,topicRep = line.split('\t')
    total_tweets+=1
    # convert count (currently a string) to int
    try:
        reDepth=float(reDepth)
	reRatio=float(reRatio)
	hashtags=float(hashtags)
	length=float(length)
	exla=float(exla)
	quest=float(quest)
	link=float(link)
	topicRep=float(topicRep)
	retweeted=float(retweeted)
    except ValueError:
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_topic == topic:
	#metrices
        aver_depth+=reDepth
	aver_ratio+=reRatio
	aver_hastags+=hashtags
	aver_length+=length
	aver_exla+=exla
	aver_quest+=quest
	aver_link+=link
	aver_topicRep+=topicRep
	#User's diversity dictionary for a topic
	if user in Dictionary_users:
		Dictionary_users[user]+=1
		users_total+=1
	else :
		Dictionary_users[user]=1
		users_total+=1
	#User's retweeted diversity dictionary for a topic
	if user in Dictionary_retweeted and retweeted==1:
		Dictionary_retweeted[user]+=1
		retweeted_total+=1
	elif retweeted==1 :
		Dictionary_retweeted[user]=1
		retweeted_total+=1
	#hashtag's/word's diversity dictionary for a topic
	words=''.join(ch for ch in text if ch not in exlude)
	words= words.split(',')
	
	for word in words:
		word=list(word)
		try:
			if word[0]=='u':
				word[0]=''
		except IndexError:
			continue
		word="".join(word).strip()
		word=list(word)
		try:
			
			if word[0]=='#':
				word="".join(word).strip()
				word=word.lower()
				
				if word in Dictionary_hashtags:
					Dictionary_hashtags[word]+=1
					hashtags_total+=1
				else :
					Dictionary_hashtags[word]=1
					hashtags_total+=1
		except IndexError:
			continue
		if type(word) is list :
			word="".join(word).strip()
		if word in Dictionary_words:
			Dictionary_words[word]+=1
			words_total+=1
		else :
			Dictionary_words[word]=1
			words_total+=1
	#Lang s retweeted diversity dictionary for a topic
	if lang in Dictionary_lang :
		Dictionary_lang[lang]+=1
		lang_total+=1
	else:
		Dictionary_lang[lang]=1
		lang_total+=1
    else:
        if current_topic:
            # write result to STDOUT
		if users_total==1:
			current_topic=topic 
			continue
		#diversities
		#calculate User's diversity index
		for key in Dictionary_users:
			users_diver+=-(float(Dictionary_users[key])/users_total)*math.log(float(Dictionary_users[key])/users_total,2)

		#calculate retweeted user's diversity index
		for key in Dictionary_retweeted:
			retweeted_diver+=-(float(Dictionary_retweeted[key])/retweeted_total)*math.log(float(Dictionary_retweeted[key])/retweeted_total,2)
		#calculate hashtag's diversity index
		for key in Dictionary_hashtags:
			hashtags_diver+=-(float(Dictionary_hashtags[key])/hashtags_total)*math.log(float(Dictionary_hashtags[key])/hashtags_total,2)
		#calculate words's diversity index
		for key in Dictionary_words:
			words_diver+=-(float(Dictionary_words[key])/words_total)*math.log(float(Dictionary_words[key])/words_total,2)
		#calculate lang's diversity index
		for key in Dictionary_lang:
			lang_diver+=-(float(Dictionary_lang[key])/lang_total)*math.log(float(Dictionary_lang[key])/lang_total,2)

		print '%s\t%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f' % (topic,cat,aver_depth/total_tweets,aver_ratio/total_tweets,aver_hastags/total_tweets,aver_length/total_tweets,aver_exla/total_tweets,aver_quest/total_tweets,aver_link/total_tweets,aver_topicRep/total_tweets,users_diver,retweeted_diver,hashtags_diver,words_diver,lang_diver)
		#initiate values for new topic	
       		aver_depth=reDepth
		aver_ratio=reRatio
		aver_hastags=hashtags
		aver_length=length
		aver_exla+=exla
		aver_quest=quest
		aver_link=link
		aver_topicRep=topicRep
		total_tweets=0
		users_total=0
		users_diver=1
		retweeted_total=0
		retweeted_diver=1
		hashtags_total=0
		hashtags_diver=1
		words_total=0
		words_diver=1
		lang_total=0
		lang_diver=1
		Dictionary_lang.clear()
		Dictionary_words.clear()
		Dictionary_hashtags.clear()
		Dictionary_users.clear()
		Dictionary_retweeted.clear()
        current_topic = topic

#last word!
if current_topic.lower() == topic.lower():
	try :
		print '%s\t%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f' % (topic,cat,aver_depth/total_tweets,aver_ratio/total_tweets,aver_hastags/total_tweets,aver_length/total_tweets,aver_exla/total_tweets,aver_quest/total_tweets,aver_link/total_tweets,aver_topicRep/total_tweets,users_diver,retweeted_diver,hashtags_diver,words_diver)
	except ZeroDivisionError or TypeError:	
		user="a"
		
