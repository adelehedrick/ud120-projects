#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

features = len(features_train[0])
print("Number of features: "+str(features))


from sklearn import tree

#params criterion= "gini" or "entropy"
#samples_split=2
clf = tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf = clf.fit(features_train, labels_train)
print("training time: "+str(round(time()-t0, 3)))

t0 = time()
acc = clf.score(features_test, labels_test)
print("testing time: "+str(round(time()-t0, 3)))

print("accuracy: "+str(acc))
#########################################################


