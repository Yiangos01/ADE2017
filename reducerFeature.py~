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
users_total=0
users_diver=1
retweeted_total=0
retweeted_diver=1
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    topic,cat,user,retweeted,reDepth,reRatio,hashtags,length,exla,quest,link,topicRep = line.split('\t')
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
	total_tweets+=1
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
	#hashtag's diversity dictionary for a topic
	
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
		#if retweeted_total==1 or retweeted_total==0:
		#	retweeted_result=0
		#else:
		#	retweeted_result=1-(float(retweeted_sum)/(float(retweeted_total)*(float(retweeted_total)-1)))		
		
		
		print '%s\t%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f' % (topic,cat,aver_depth/total_tweets,aver_ratio/total_tweets,aver_hastags/total_tweets,aver_length/total_tweets,aver_exla/total_tweets,aver_quest/total_tweets,aver_link/total_tweets,aver_topicRep/total_tweets,users_diver,retweeted_diver)
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
		Dictionary_users.clear()
		Dictionary_retweeted.clear()
        current_topic = topic

#last word!
if current_topic.lower() == topic.lower():
	try :
		print '%s\t%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f' % (topic,cat,aver_depth/total_tweets,aver_ratio/total_tweets,aver_hastags/total_tweets,aver_length/total_tweets,aver_exla/total_tweets,aver_quest/total_tweets,aver_link/total_tweets,aver_topicRep/total_tweets,users_diver,retweeted_diver)
	except ZeroDivisionError or TypeError:	
		user="a"
		
