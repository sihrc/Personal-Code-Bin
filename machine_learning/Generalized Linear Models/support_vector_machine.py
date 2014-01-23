"""
Support Vector Machine
Classification
1.2.1
Chris Lee
"""

import template
import numpy as np
from sklearn import svm

if __name__ == "__main__":
	print "Receiving Data ..."
	trainX, trainY, m = template.ReceiveData()
	
	limit = 1000
	print "Creating Model"
	clf = svm.SVC()
	print "Fitting Data"
	clf.fit(trainX[:-limit], trainY[:-limit])
	print "Predicting Test Data"
	predictions = clf.predict(trainX[limit:])
	print "Prediction Error:", len(np.where(predictions - trainY[limit:] != 0))/limit

