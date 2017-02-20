#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import tweepy
import json
import time
import MySQLdb

#Variables that contains the user credentials to access Twitter API 
access_token = "766999276245221376-vBrbI2C7vCllPRb56O5sko2Ocn40uuJ"
access_token_secret = "weo8dbLeNA2ancEgJyMj258kw3r1zW3D9OX3SvUEXnrlB"
consumer_key = "tUbhzENsSXbdQ2dEmOP2fiOYz"
consumer_secret = "RYCYrdpmtNl3R6usXwlPcuMiQp8TXrgat4YPfZo3zyYWWDU1xn"




#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':  
    
    conn = MySQLdb.connect(host= "localhost",user="root",passwd="px2h-r7s",db="twitter_data")
    x = conn.cursor()
    trendlistNew=[]
    trendlist=[]
    print(len(trendlist))
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=False)
    
    while 1 :
    	trends1 = api.trends_place(id=44418)
    	data = trends1[0]

    	trends = data['trends']
    	hashtags=0
	urls=0
	retweeted=0
    	names = [trend['name'] for trend in trends]
    	trendlistNew=[trend for trend in names if trend not in trendlist]
	print trendlistNew
    	for topic in trendlistNew:
		try:
			first=True
    			#new_tweets=json.dumps(new_tweets) 
    			for tweet in  tweepy.Cursor(api.search,q=topic,rpp=400,result_type="recent",include_entities=True).items(400):
				#if tweet["lang"]=='en' or tweet["lang"]=='gr' :
				try:    
					userId= tweet.user.id
					tweetId=tweet.id
					text = tweet.text.encode('utf-8')
					text = text.replace('\n', ' ').replace('\r',' ')
					text = text.replace('\t', ' ').replace('\r',' ')
					text = text.replace('"', ' ').replace('\r',' ')
					for hashtag in tweet.entities["hashtags"]:
						hashtags += 1
					for link in tweet.entities["urls"] :
						urls +=1
					try:	
						tweet.retweeted_status
					except AttributeError:
						retweeted=0
					else :
						retweeted=1
					lang = tweet.lang
					timestamp = tweet.created_at
					timestamp=str(timestamp).split(' ')
					
					if first :
						first=False
						try:
							x.execute("INSERT INTO `topics` (`name`) VALUES (\""+str(topic)+"\")")
							conn.commit()	
							print "succees on topic"
						except:
							print "error on topic"
							print conn.rollback()
					try:
						x.execute("INSERT INTO `tweets` (`id`, `tweet_id`, `user_id`, `tweet_text`, `hashtags_count`, `url_count`, `is_retweeted`, `lang`, `retweet_count`, `favorite_count`, `date`, `time`, `topic`) VALUES (NULL,\""+str(tweetId)+"\",\""+str(userId)+"\",\""+str(text)+"\",\""+str(hashtags)+"\",\""+str(urls)+"\",\""+str(retweeted)+"\",\""+str(lang)+"\",\""+str(tweet.retweet_count)+"\",\""+str(tweet.favorite_count)+"\",\""+str(timestamp[0])+"\",\""+str(timestamp[1])+"\",\""+str(topic)+"\")")
						conn.commit()	
						print "succees on tweet"
					except:
						print "error on tweet"
						print conn.rollback()
					hashtags=0
					urls=0
					retweeted=0
				except ValueError:
					print "error"
					continue
		except ValueError:
			continue
				
	trendlist += trendlistNew 
	trendlistNew=[]
	time.sleep(60*15)
