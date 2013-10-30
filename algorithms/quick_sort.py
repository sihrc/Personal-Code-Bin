"""
Quick Sort

Author: Chris Lee
Created: 10/21/2013
"""

def quickSort(unsorted):	
	if len(unsorted) == 1:
		return unsorted
	midIndex = len(unsorted)/2
	head = []
	tail = []
	[head.append(x) if x <= unsorted[midIndex] else tail.append(x) for x in unsorted]
	return quickSort(head) + [unsorted[midIndex]] + quickSort(tail)

if __name__ == "__main__":
	unsorted = [3,2,43,56,3,43,234,246,42,351,125,124,2315,135,531,35,325,32,35,1,12,125,45,125,3125,32,4]
	print quickSort(unsorted)