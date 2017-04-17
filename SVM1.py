from pandas import DataFrame
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier
from sklearn import svm
import pandas as pd
import numpy as np
import copy
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesClassifier
def build_data_frame(file_name):
	with open(file_name,'rb') as tweets:	
		firstline=True
		topics=[]
		rows=[]
		for topic in tweets:
			if firstline:
				firstline=False
			else:
				topic=topic.strip().split('\t')
				features=topic[2:]
				if topic[1] == 'live events':
          				rows.append({"features":features,"category":0})
        			elif topic[1] == 'group interest':
          				rows.append({"features":features,"category":1})
        			elif topic[1] == 'news':
            				rows.append({"features":features,"category":2})
       				elif topic[1] == 'commemoratives':
            				rows.append({"features":features,"category":3})
					
				topics.append(topic[0])
		dataframe = DataFrame(rows,index=topics)
	return dataframe

if __name__=='__main__':

	data=build_data_frame('features_data2.csv')
	data=data.sample(frac=1) #shuffle dataset
	feature = data['features'].values
	categories = data['category'].values
	#data=data.sample(frac=1) #shuffle dataset
	features=[]
	count=1
	for l in feature:
		l=[float(i) for i in l]
		features.append(l)
		count+=1
	features=pd.DataFrame(features)
	#normalize data
	scaler = MinMaxScaler(feature_range=(1,10))
	features = scaler.fit_transform(features)

	#feature selection
	test = SelectKBest(k=10)
	fit = test.fit(features, categories)
	features = fit.transform(features)
	
	#classification
	train_x,test_x,train_y,test_y=train_test_split(features,categories,test_size=0.25,random_state=42)
	#print train_x
	#test_x=np.array(test_x)
	#test_y=np.array(test_y)
	#print train_x[0]
	#print (train_y)
	#print(str(len(x_train))+'\t'+str(len(x_test))+'\t'+str(len(y_train))+'\t'+str(len(y_test)))
	#clf=svm.SVC(kernel='rbf',gamma=0.01,C=100,max_iter=-1)
	#clf=svm.SVC(kernel='rbf',gamma=0.001,C=100,max_iter=-1)
	#clf=svm.SVR(
	#clf=svm.LinearSVC(max_iter=-1,class_weight='balanced')
	clf=RandomForestClassifier(n_estimators=200)
	#clf=ExtraTreesClassifier(n_estimators=30)
	clf.fit(train_x,train_y)
	#score=cross_val_score(clf,features,categories,cv=6)
	#clf.decision_function(train_x)
	prediction=clf.predict(test_x)
	print prediction
	print test_y
	score=accuracy_score(test_y,prediction)
	#print prediction
	print score




