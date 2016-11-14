#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

from sklearn.svm import SVC
#clf = SVC(kernel="linear")

C = 10000.0
clf = SVC(kernel="rbf", C=C)

print("C: "+str(C))

# train on only 1% of the data set
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print("training time: "+str(round(time()-t0, 3)))


t0 = time()
pred = clf.predict(features_test)
print("testing time: "+str(round(time()-t0, 3)))

acc = clf.score(features_test, labels_test)
print("accuracy: "+str(acc))
#########################################################

total = len(pred)
chris = sum(pred)
print("out of "+str(total)+" test events, a sum of 1's gives us chris")
print("chris = "+str(chris))
print("sara  = "+str(total-chris))


a1 = pred[10]
print("10: "+str(a1))
a2 = pred[26]
print("26: "+str(a2))
a3 = pred[50]
print("50: "+str(a3))
