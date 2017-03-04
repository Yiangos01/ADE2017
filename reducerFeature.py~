#!/usr/bin/env python

from operator import itemgetter
import sys

current_topic = None
current_count = 0
total_tweets=0
aver_depth=aver_ratio=aver_hastags=aver_length=aver_exla=aver_quest=aver_link=aver_topicRep=0
word = None
Dictionary_users = {}
users_total=0
users_sum=0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    topic,cat,user,reDepth,reRatio,hashtags,length,exla,quest,link,topicRep = line.split('\t')

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
    except ValueError:
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_topic == topic:
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
	else :
		Dictionary_users[user]=1
    else:
        if current_topic:
            # write result to STDOUT
		#Calculate User's Simpson diversity index
		for key in Dictionary_users:
			users_total+=Dictionary_users[key]
			users_sum+=Dictionary_users[key]*(Dictionary_users[key]-1)
		user_result=1-float(users_sum)/(float(users_total)*(float(users_total)-1))	
		#print '%s' % (topic)
		print '%s\t%s\t%s\t%s' % (str(users_total),str(users_sum),topic,user_result)
		print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (topic,cat,aver_depth/total_tweets,aver_ratio/total_tweets,aver_hastags/total_tweets,aver_length/total_tweets,aver_exla/total_tweets,aver_quest/total_tweets,aver_link/total_tweets,aver_topicRep/total_tweets,user_result)
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
		users_sum=0
		Dictionary_users.clear()
        current_topic = topic

#last word!
if current_topic.lower() == topic.lower():
	try :
	#print '%s\t%s\t%s' % (str(users_total),str(users_sum),topic)
		print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (topic,cat,aver_depth/total_tweets,aver_ratio/total_tweets,aver_hastags/total_tweets,aver_length/total_tweets,aver_exla/total_tweets,aver_quest/total_tweets,aver_link/total_tweets,aver_topicRep/total_tweets,(1-(float(users_total)/float(users_sum))))	
	except ZeroDivisionError :
		user="a"
		
