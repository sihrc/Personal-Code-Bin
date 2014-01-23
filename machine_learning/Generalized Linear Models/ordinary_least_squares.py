"""
Ordinary Least Squares
Linear
1.1.1
Chris Lee
"""
from sklearn import linear_model
import numpy as np
import template

if __name__ == "__main__":
	print "Retrieving Data from Server ..."
	trainX, trainY, count = template.ReceiveData()
	
	#print "Visualizing Data ..."
	#template.VisualizeData(trainX, trainY, 0)

	print "Fitting Model"
	clf = linear_model.LinearRegression()
	clf.fit(trainX[:-1000], trainY[:-1000])
	print "Finished fitting the model"
	print "Prediction Mean Square Error:"
	print np.mean((clf.predict(trainX[-1000:]) - trainY[-1000:])**2)
