"""
Template for reading data from load_data_server.py
Chris Lee
"""

import numpy as np
from multiprocessing.connection import Client
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from timer import print_timing

@print_timing
def ReceiveData():
	c = Client(('127.0.0.1', 5000))
	c.send('data')
	return c.recv()

#Data is a numpy array containing the "n" number of pixel values.
def VisualizeData(data, target, n):	
	print "Visualizing Training Set ", n, "\nExpected Number: ", target[n]
	plt.imshow((data[n]/255.0).reshape(28,28), cmap = cm.Greys_r)
	plt.show()

def run():
	print "Retrieving Data from Server"
	trainX, trainY, m = receiveData()
	print "Loaded ", m, "records."
	print "Features: --------------------"
	print trainX
	print "Targets: --------------------"
	print trainY

if __name__ == "__main__":
	run()