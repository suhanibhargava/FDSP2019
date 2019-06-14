# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:15:30 2019

@author: Dell
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("amazon_cells_labelled.txt", header = None, delimiter = '\t')

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset[0][i])
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
labels = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)


#using knn
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)



from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(features_train , labels_train)
labels_predicted = model.predict(features_test)
cm_nb = confusion_matrix(labels_test, labels_pred)



review = "Good case, Excellent value"
corpus =[]
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

review = re.sub('[^a-zA-Z]', ' ', review)
review = review.lower()
review = review.split()
review = [word for word in review if not word in set(stopwords.words('english'))]
    
#lem = WordNetLemmatizer() #Another way of finding root word
ps = PorterStemmer()
review = [ps.stem(word) for word in review]
#review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
review = ' '.join(review)
corpus.append(review)
    
feature = cv.transform(corpus).toarray()
prediction = classifier.predict(feature)

