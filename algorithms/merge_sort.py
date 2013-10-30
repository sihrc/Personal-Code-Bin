"""
Merge Sort
author: Chris Lee
created: 10/12/2013
"""
import numpy.random as nprnd
import itertools
import timer

@timer.print_timing
def mergeSort(unsorted):
	unsorted = [[x] for x in unsorted]

	while len(unsorted) > 1:
		unsorted = foldList(unsorted)
	return unsorted
	
	
def foldList(unsorted):
	step = []
	for x,y in zip(unsorted[::2],unsorted[1::2]):
		#print "Comparing", x,y
		step.append(comparePair(x,y))
		#print "Results in", step
	if len(unsorted) % 2 != 0:
			extra = comparePair(step.pop(), unsorted.pop())
			step.append(extra)
	return step


def comparePair(A,B):
	res = []
	i, j = 0, 0
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			res.append(A[i])
			i += 1
		else:
			res.append(B[j])
			j += 1
	res += A[i:] if i < j else B[j:]
	return res



if __name__ == "__main__":
	mergeSort(nprnd.randint(1000, size = 100000))
	