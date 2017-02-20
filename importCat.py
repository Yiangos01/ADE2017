import MySQLdb
import csv

if __name__ == '__main__':  
	
	conn = MySQLdb.connect(host= "localhost",user="root",passwd="px2h-r7s",db="twitter_data")
	x = conn.cursor()
	f=open("alltopics.csv")
	csv.reader(f)
	for row in f:
		text = row.replace('\n', ' ').replace('\r',' ')
		cat=text.split("\t")
		cat[1] = cat[1].replace(' ','')
		
		
		try:
			x.execute("UPDATE `topics` SET `category`=\""+cat[1]+"\" WHERE name = \""+cat[0]+"\"")
			conn.commit()	
			#print "succees on topic"
		except:
			print row
			print conn.rollback()
	f.close()
