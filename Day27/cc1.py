# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:29:18 2019

@author: Dell
"""

import pandas as pd
import numpy as np
import json

train_data = pd.read_json("train.json" , lines= True , orient = 'columns')
test_data = pd.read_json("test_data.json" , lines= True , orient = 'columns')

features_train = train_data.iloc[:,:-1].values
labels_train = train_data.iloc[:,0].values
features_test = test_data

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]

for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', train_data['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = train_data.iloc[:,0].values


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
