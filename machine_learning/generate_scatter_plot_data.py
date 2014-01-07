"""
Generates Scatter Plot fit around a given function
and a given number of inputs
"""
import random, pickle, itertools, Queue, threading
import numpy as np

#Calculates the Function from coefficients of the iterator
def calculate(x, iterator, q):
	data = []
	try:
		while True:
			coeffs = iterator.next()
			xvalues, yvalues = zip(*coeffs)
			data.append(list(xvalues) + [sum(yvalues)])
			#print "Created: ", coeffs, res, "..."
	except StopIteration:
		pass
	q.put(data)


if __name__ == "__main__":
	#Number of features
	#Feature Range (the range of input values the data should have)
	#Coefficients (the coefficients of the features)

	num_features = 5
	coefficients = []
	for x in xrange(num_features):
		coefficient = (2*(random.random() - .5))
		exponent = 1
		xs = 2000*np.linspace((random.random()-.5),(random.random()-.5), random.randint(5,30))
		coefficients.append((coefficient, exponent, zip(xs, [coefficient * value ** exponent for value in xs])))

	q = Queue.Queue()
	exec("iterator = itertools.product(" + ",".join([str(x[2]) for x in coefficients]) + ")")
	for x in xrange(4):
		t = threading.Thread(target = calculate, args = (x, iterator, q))
		t.daemon = True
		t.start()

	s = q.get()
	s.append(coefficients)
	print "Data Generated:\n Coefficients:", [str(coefficient[0]) for coefficient in coefficients]
	with open("scatter_plot", 'wb') as f:
		print "Pickling... Please wait..."
		pickle.dump(s, f)

