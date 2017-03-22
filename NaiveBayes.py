from pandas import DataFrame
import re
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, accuracy_score

#Create a dataframe which in the first column contains the text and in the second the category
def build_data_frame(file_name):
	with open(file_name,'rb') as tweets:	
		firstline=True
		topics=[]
		rows=[]
		for tweet in tweets:
			if firstline:
				firstline=False
			else:
				fields = tweet.strip().split('\t')
      	 			line = fields[5]
				line = re.sub(r"{rt}", "", line)
		 	       	line = re.sub(r"http\S+", "", line)
				line = re.sub(r"([!.'():,?]+)", " ", line)
				line = re.sub(r"https\S+", "", line)
		       		line = re.sub(r"(@[a-zA-Z0-9_]+)", "", line)
		       		line = re.sub(r"([0-9]+)", "", line)
		       		line = line.lower()
	  	     		line = re.sub(r"(.)\1{1,}", r"\1\1", line)
				line = line.strip()
				rows.append({"text":line,"category":fields[1]})
				topics.append(fields[14])
		dataframe = DataFrame(rows,index=topics)
	return dataframe

if __name__=='__main__':
	data=build_data_frame('dataset.csv')
	#data=data.sample(frac=1) #shuffle dataset
	pipeline = Pipeline([	('vectorizer',CountVectorizer()),
				('classifier',MultinomialNB())
			   ])
	#Cross-Validating 
	kfold = KFold(n=len(data),n_folds=10)
	scores = []
	for train_ind,test_ind in kfold:
		train_text = data.iloc[train_ind]['text'].values
		train_y= data.iloc[train_ind]['category'].values

		test_text = data.iloc[test_ind]['text'].values
		test_y= data.iloc[test_ind]['category'].values
		
		pipeline.fit(train_text,train_y)
		predictions = pipeline.predict(test_text)
		
		print (predictions)
		score = accuracy_score(test_y, predictions)
		print score
		scores.append(score)
print ("Score: {:.2f}".format(sum(scores)/len(scores)))
	
