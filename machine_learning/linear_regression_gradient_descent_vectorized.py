"""
Supervised Learning
Linear Regression with Gradient Descent
with Vectorization

Lesson 11
http://openclassroom.stanford.edu/MainFolder/VideoPage.php?course=MachineLearning&video=02.6-LinearRegressionI-VectorizedImplementation&speed=100

This is about twice as fast as the non-vector 
Thanks Andrew Ng.
"""
import numpy as np, pickle

if __name__ == "__main__":
	with open("scatter_plot", 'rb') as f:
		load = pickle.load(f)
	#Convert Data to a Matrix
	data = np.matrix(load[:-1])
	#Grab the expected Theta
	expected = load[-1]
	#Grab the rows and columns of the data (features and samples)
	m,n = data[:-1,:-1].shape

	#Initialize Theta
	theta = np.matrix([0.0]*n)
	previous_theta = np.matrix([0.0]*n)
	previous_delta = 0.0

	#Random starting step
	alpha = 10.0

	#Accuracy in decimal places
	accuracy = 10.0

	while True:
		#Updating Theta 
		delta = alpha/m * ((data[:,:-1] * theta.transpose() - data[:,-1]).transpose() * data[:,:-1])
		theta -= delta

		#Checking change
		delta = abs(delta).sum()
		if delta > previous_delta and previous_delta != 0:
			alpha *= previous_delta/delta
			print "Lowered Alpha", alpha
		print "-----------------"
		print "Theta\n", theta

		if (abs(theta - previous_theta).sum()) < 10**-accuracy:
			print "Sufficient alpha determined at", alpha
			break;
		else:
			previous_delta = delta
			previous_theta = theta.copy()
	




	