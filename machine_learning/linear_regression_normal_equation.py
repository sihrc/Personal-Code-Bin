"""
Supervised Learning
Linear Regression by Normal Equation

Lesson 15
http://openclassroom.stanford.edu/MainFolder/VideoPage.php?course=MachineLearning&video=02.6-LinearRegressionI-VectorizedImplementation&speed=100

Thanks Andrew Ng.
"""

import pickle, numpy as np, sys

if __name__ == "__main__":
	with open("scatter_plot", 'rb') as f:
		print "Loading Data... One Moment Please..."
		load = pickle.load(f)
		print "Load Complete"
	#Grab the expected Theta
	expected = [a for a,b,c in load[-1]]
	#Convert Data to a Matrix
	data = np.matrix(load[:-1])
	#Grab the rows and columns of the data (features and samples)
	m,n = data[:-1,:-1].shape

	if m < n:
		print "Singular Matrix Detected. Completion impossible."
		print "Exiting ... "
		sys.exit()
	#Grab Input and Target Values
	xvalues = data[:,:-1]
	yvalues = data[:,-1]
	#Calculate Optimal Minimum
	theta = (xvalues.transpose() * xvalues)**-1 * xvalues.transpose() * yvalues
	print "Calculated Values:", theta
	print "Expected Values", expected

