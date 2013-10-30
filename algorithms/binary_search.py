"""
Binary Search
author: Chris Lee
created: 10/11/2013

usage: python binary_search [max value] [list length]
"""
import sys   #Get input
import numpy #Generating list of random integers

def binary_search(xs,x):
	size = len(xs)
	if x < xs[size/2] and size > 1:
		return binary_search(xs[:size/2], x)
	elif x > xs[size/2] and size > 1:
		return size/2 + binary_search(xs[size/2:], x)
	else:
		return size/2
	return -11

if __name__ == "__main__":
	try:
		ordered_list =  numpy.random.randint(int(sys.argv[1]), size = int(sys.argv[2]))
	except:
		print "Please enter integers!"
		sys.exit()

	ordered_list.sort()
	print "Here's the list I made:\n", ordered_list

	print "Searching for random matches [input 'n' to cancel]"
	while raw_input() != "n":
		value = ordered_list[numpy.random.randint(int(sys.argv[2]))]
		index = binary_search(ordered_list, value)
		if ordered_list[index] == value:
			print "I found %d at index %d in the list!" % (value, index)


