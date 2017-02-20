import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt2
from collections import Counter

csv_file=pd.read_csv("topic_data.csv",sep='\t')
c=Counter(csv_file["lang"]).most_common(6)
x_axis=[]
y_axis=[]
for val in c:
	x_axis.append(val[0])
	y_axis.append(val[1])
#lang
fig,ax = plt.subplots()
index=np.arange(len(x_axis))
bar_width=0.7
opacity=0.8
error_config={'ecolor':'0.3'}
recults=plt.bar(index,y_axis,bar_width,alpha=opacity,color='r',error_kw=error_config)
plt.ylabel('value')
plt.xlabel('lang')
plt.xticks(index+0.4/1.2,x_axis)
plt.legend()
plt.title('6 most common languages')
plt.tight_layout()

#dates
x_axis_date=[]
y_axis_date=[]
dates=Counter(csv_file["date"]).most_common(7)
#print dates
for val in dates:
	x_axis_date.append(val[0])
	y_axis_date.append(val[1])
#print x_axis_date , y_axis_date
fig,ax = plt.subplots()
index=np.arange(len(x_axis_date))
bar_width=0.5
opacity=0.8
error_config={'ecolor':'0.3'}
recults=plt.bar(index,y_axis_date,bar_width,alpha=opacity,color='b',error_kw=error_config)
plt.xlabel('Days')
plt.ylabel('values')
plt.title('tweets per day')
plt.xticks(index+0.3/1.2,x_axis_date)
plt.legend()
plt.tight_layout()
plt.show()

#categories
x_axis_cat=[]
y_axis_cat=[]
categories=Counter(csv_file["category"])
print categories


