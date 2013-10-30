"""
Simulating a 7-sided die using a 5-sided die

author: Chris Lee
created: 10/12/2013
"""
import numpy as np
import itertools


def sevenDie(outcomes):
	roll = outcomes[np.random.randint(5),np.random.randint(5)]
	return roll if roll != 0 else sevenDie(outcomes)

if __name__ == "__main__":
	mapOutcomes = np.zeros(shape = (5,5))
	mapOutcomes[0] = [1,1,1,6,7]
	mapOutcomes[1] = [2,2,2,6,7]
	mapOutcomes[2] = [3,3,3,6,7]
	mapOutcomes[3] = [4,4,4,0,0]
	mapOutcomes[4] = [5,5,5,0,0]

	#Testing Randint probability
	probDict = dict()
	for _ in itertools.repeat(None, 100000):
		roll = sevenDie(mapOutcomes)
		probDict[roll] = probDict.get(roll,0) + 1
	for res in xrange(1,8):
		print res,":",probDict[res]
	

