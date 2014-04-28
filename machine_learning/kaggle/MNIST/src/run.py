import numpy as np
import os

from sklearn.linear_model import Ridge
from sklearn import metrics
import matplotlib.pyplot as plt

def one_hot(array):
        """
        [0,1,2,3,4,5,6,7,8,9]
        """
        array = array.flatten()
        output = np.zeros(shape = (len(array),np.max(array) + 1))
        output[np.arange(len(array)),array] = 1
        return output

def load(onehot=False):
        """
        OneHot = binary indicator
        extracts 
        """
        path = os.path.join("..","data")
        fd = open(os.path.join(path,'train.idx3-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        trainX = loaded[16:].reshape((60000,28*28))/255.

        fd = open(os.path.join(path,'train.idx1-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        trainY = loaded[8:].reshape((60000))

        fd = open(os.path.join(path,'test.idx3-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        testX = loaded[16:].reshape((10000,28*28))/255.

        fd = open(os.path.join(path,'test.idx1-ubyte'))
        loaded = np.fromfile(file=fd,dtype=np.uint8)
        testY = loaded[8:].reshape((10000))

        if onehot:
                trainY = one_hot(trainY)
                testY = one_hot(testY)

        return trainX,testX,trainY,testY

if __name__ == "__main__":
	#Loading the data
	trainX,testX,trainY,testY = load(onehot = True)

        #Sanity Check
        print "Loaded Data"
        print "trainX"  , trainX.shape
        print "testX"   , testX.shape
        print "trainY"  , trainY.shape
        print "testY"   , testY.shape

        #Modeling
        model = Ridge(alpha = 1000) # alpha is penalty
        model.fit(trainX, trainY)
        weights = model.coef_
        print weights.shape
        print weights
        plt.imshow(weights[0].reshape(28,28), cmap="gray")
        plt.show()
        raw_input()
        #Predictions
        predictions = model.predict(testX)

        #Evaluation functions
        #Linear regression - print root mean square error + whatever
        print metrics.accuracy_score(np.argmax(testY, axis = 1), np.argmax(predictions, axis = 1))





