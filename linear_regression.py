#!/usr/bin/env python
"""
See scikit-learn docs re. the advantages of
threaded / parallel algorithms (N jobs).

Similar to y = mX + b

Except in this case, rather than x or y axis in geometry...

X = features (in dataframe)
y = label

##########

For interactive graphing in the Python interpreter without iPython...

In the matplotlibrc file...

Set the backend to TkAgg 
Set interactive to True

You can find it in...

/home/<username>/.virtualenvs/machine_learning/lib/python3.4/site-packages/matplotlib/mpl-data/matplotlibrc

Also, you'll need to make sure tkinter is installed...

sudo apt-get install python3-tk

You may also need to install SIP (sip-4.19.1) 
and/or PyQt4 (PyQt4_gpl_x11-4.12).

"""
import pandas as pd
import numpy as np
import quandl, math, datetime
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#from matplotlib import style, interactive

#matplot style
plt.style.use('ggplot')

##########
#fetch raw dataframe
df = quandl.get('WIKI/GOOGL')

##########
#tease out features from raw dataframe
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

##########
#define new feature--High Low Percent
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

#define new feature--Percent Change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

##########
#repackage dataframe with required features
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

##########
#assign forecast_col variable
forecast_col = 'Adj. Close'

##########
#this handles empty values / missing data
df.fillna(-99999, inplace=True)

##########
#assign forecast_out variable
#this is a rather arbitrary value relative to the dataframe
#in this case: 1% of the total days represented in the data
#approx. 30 days
forecast_out = int(math.ceil(0.01*len(df)))

##########
#assign prices 30 days out to label column
#takes "Adj. Close" price and shifts it out (into the future)
#by the forecast_out value
df['label'] = df[forecast_col].shift(-forecast_out)

##########
#drop the label column and return a new dataframe
X = np.array(df.drop(['label'],1))

##########
#scale data
X = preprocessing.scale(X)

#colon interpreted as "to the point"
#X_lately ]gis what we're predicting against; no y value
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

##########
#clean up empty values in dataframe
df.dropna(inplace=True)
#assign label
y = np.array(df['label'])

##########
#create training and testing set
#use 20% of the dataframe as testing data
#takes features and labels and shuffles via cross_validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

##########
#define the classifier
#can use Linear Regression...
#n_jobs = -1 will run as many jobs in paralllel as processor will allow
#~~~~~~~~
clf = LinearRegression(n_jobs='-1')
#~~~~~~~~
#or can use Support Vector Regression
#with polynomial kernal
#~~~~~~~~
#clf = svm.SVR(kernel='poly')

##########
#train the data
#fit is synonymous with train
clf.fit(X_train, y_train)

##########
#determine the accuracy
#accuracy is "squared error"
#score is synonymous with test
accuracy = clf.score(X_test, y_test)

##########
#produce the forecasted data
#returns predicted stock prices 30 days out
forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)

#fill Forecast column with "Not A Number" values
df['Forecast'] = np.nan

#since the model really doesn't know the date, we hardcode it
#the date is not a feature in the dataframe
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

#now we iterate through the forecast set
#taking each day and forecast
#setting those values in the dataframe
#in other words...
#making the future features a NAN (Not A Number)
#in other words...
#last line in the following for loop re-explained:
#sets first column in dataframe to NAN, and...
#sets last column to whatever 'i' is, which is the forecast
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    #loc is index for dataframe
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
    
df['Adj. Close'].plot()
df['Forecast'].plot() 
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')    
plt.show(block=True)

#print(df.head())
#print(len(X), len(y))
#plt.savefig('graph.png')
