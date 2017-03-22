from sklearn import svm
from pandas import DataFrame
from sklearn.cross_validation import train_test_split
import pandas as pd
import copy
def build_data_frame(file_name):
	with open(file_name,'rb') as tweets:	
		firstline=True
		topics=[]
		rows=[]
		for topic in tweets:
			if firstline:
				firstline=False
				print topic
			else:
				topic=topic.strip().split('\t')
				features=topic[2:]
				rows.append({"features":features,"category":topic[1]})
				topics.append(topic[0])
		dataframe = DataFrame(rows,index=topics)
	return dataframe

if __name__=='__main__':

	data=build_data_frame('features.csv')
	data=data.sample(frac=1) #shuffle dataset
	feature=data['features'].values
	categories=data['category'].values
	
	features=[]
	for l in feature:
		l=[float(i) for i in l]
		features.append(l)
	features=pd.DataFrame(features)
	features = (features - features.mean()) / (features.max() - features.min())
	print features
	train_x,test_x,train_y,test_y=train_test_split(features,categories,test_size=0.30,random_state=42)
	#test_x=np.array(test_x)
	#test_y=np.array(test_y)
	#print train_x[0]
	#print (train_y)
	#print(str(len(x_train))+'\t'+str(len(x_test))+'\t'+str(len(y_train))+'\t'+str(len(y_test)))
	clf=svm.SVC(kernel='sigmoid',C=1.0,gamma=0.0001,max_iter=-1)
	clf.fit(train_x,train_y)
	score=clf.score(test_x,test_y)
	print score

	
