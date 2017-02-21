import MySQLdb
import csv

if __name__ == '__main__':  
	
	conn = MySQLdb.connect(host= "localhost",user="root",passwd="px2h-r7s",db="twitter_data")
	x = conn.cursor()
	f=open("alltopic.csv")
	csv.reader(f)
	i=0
	for row in f:
		i=i+1
		text = row.replace('\n', ' ').replace('\r',' ')
		cat=text.split("\t")
		if len(cat)>1:
			if cat[1]=="ongoing events" or cat[1]=="ongoing events "  :
				cat[1]="live events"
				#print cat
			elif cat[1]=="group interest" or cat[1]=="group interest " :
				cat[1]="group interest"
			elif cat[1]=="news" or cat[1]=="news ":
				cat[1]="news"
			elif cat[1]=="commemoratives" or cat[1]=="commemoratives " or  cat[1]=="commemoratives\t":
				cat[1]="commemoratives"
			elif  cat[1]==" ":
				cat[1]=None

				
		else :
			print cat

		try:
			x.execute("UPDATE `topics` SET `category`=\""+cat[1]+"\" WHERE name = \""+cat[0]+"\"")
			conn.commit()	
			
		except:
			print " "
			#print conn.rollback()
	f.close()
