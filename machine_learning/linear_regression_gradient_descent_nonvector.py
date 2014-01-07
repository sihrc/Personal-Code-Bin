"""
Supervised Learning
Linear Regression with Gradient Descent
without Vectorization

Lesson 10
http://openclassroom.stanford.edu/MainFolder/VideoPage.php?course=MachineLearning&video=02.6-LinearRegressionI-VectorizedImplementation&speed=100

Thanks Andrew Ng.
"""
import random, pickle


#Dot Product
def dot(x,y):
	return sum([x[i]*y[i] for i in xrange(len(x))])

def close(x,y,n):
	if len(x) != len(y):
		return false
	else:
		return [int (xs * 10**n) for xs in x] == [int (ys * 10**n) for ys in y]

# Given n features, represented by x_1, x_2, ... , x_n
# and the target value y, we're going to find theta_1, theta_2, theta_3, ... ,theta_n
# such that the predicted value and given value is minimized.

if __name__ == "__main__":
	with open("scatter_plot", "rb") as f:
		data = pickle.load(f)
	expected_theta = data[-1]
	n = len(data[0]) - 1
	m = len(data) - 1
	alpha = 10.0 # Gradient Step Size
	thetas = n*[0] # Theta
	previous = thetas
	previous_delta = 0
	while True:
		thetas = [thetas[j] - alpha/m * sum([(dot(thetas, data[i][:-1]) - data[i][-1]) * data[i][j] for i in xrange(m)]) for j in xrange(n)]
		delta = sum([abs(thetas[x] - previous[x]) for x in xrange(n)])
		if delta > previous_delta and previous_delta != 0:
			alpha *= previous_delta/delta
			print "LOWERED ALPHA", alpha
		print "--------------------"
		print "thetas", thetas
		if close(thetas,previous,10):
			print "New Alpha for this set - ", alpha
			break;
		else:
			previous_delta = delta
			previous = thetas
