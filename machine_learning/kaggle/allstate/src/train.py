import os
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

from wrappers import debug

@debug
def load(filename):
	"""Load Data from .csv"""
	#Load data into panda and numpy array
	data = pd.io.parsers.read_csv(filename, header = 0).values
	X = np.hstack((data[:,-8:-1], data[:,-2:-1]))
	Y = data[:,-8:-1]

	#One Hot the plan options
	enc = OneHotEncoder()
	enc.fit(Y)
	Y = enc.transform(Y).toarray()

	return X, Y

@debug
def train(trainX, trainY):
	"""Train Model"""
	model = RandomForestClassifier()
	model.fit(trainX, trainY)
	return model

@debug
def predict(model, testX):
	"""Make Predictions"""
	prediction = model.predict(testX)
	return prediction

@debug
def calculateError(prediction, testY):
	"""Calculate Error"""
	return accuracy_score(testY, prediction)

@debug
def write(prediction, testX):
	"""Write Submission"""
	data = pd.io.parsers.read_csv(os.path.join("..","data","sampleSubmission.csv")).values

if __name__ == "__main__":
	trainX, trainY = load(os.path.join("..","data","train.csv"))
	testX , testY  = load(os.path.join("..","data","test.csv"))

	model = train(trainX, trainY)
	prediction = predict(model, testX)
	error = calculateError(prediction, testY)

	print model.coef_




