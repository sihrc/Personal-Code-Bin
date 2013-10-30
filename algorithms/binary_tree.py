"""
Binary Trees
author: Chris Lee
created: October 11, 2013
"""

"""
Implementing Binary Trees
"""
import numpy.random as rand
import itertools


class BinaryTree:
	def __init__ (self, depth = 0, parent = None):
		self.depth = depth
		self.assignValue()

		self.parent = parent
		self.left = BinaryTree(depth = depth - 1, parent = self) if depth > 0 else None
		self.right = BinaryTree(depth = depth - 1, parent = self) if depth > 0 else None

	#Assign unique value to node
	def assignValue(self):
		index = rand.randint(len(uniqueList))
		self.value = uniqueList[index]
		del(uniqueList[index])

	#Find common parent without storing nodes
	def getRandomNodes(self, number):
		nodes = []
		for _ in itertools.repeat(None,number):
			node = self
			for _ in itertools.repeat(None,rand.randint(self.depth)):
				node = node.left if rand.randint(2) == 0 else node.right
			nodes.append(node)
		return nodes

	def commonParent(self, nodes):
		print "="*(50 + 2*len(nodes)), "\n  Searching for a common parent for nodes:", ",".join([str(x.value) for x in nodes]), "\n", "="*(50 + 2*len(nodes))

		#Check Node inputs
		if None in [x.parent for x in nodes]:
			print "Warning: root node has no parent."

		if len(set(nodes)) != len(nodes):
			print "Warning: nodes are identical"

		#Bring to the same depth
		maxDepth = max([x.depth for x in nodes])
		while min([x.depth for x in nodes]) != maxDepth:
			nodes = [x.parent if x.depth < maxDepth else x for x in nodes]		

		#Set for uniqueness
		nodes = set(nodes)
		while len(nodes) > 1:
			nodes = set([x.parent for x in list(nodes)])

		print "Common Parent:"
		return list(nodes)[0]


	"""
	Printing Binary Trees
	Simple Printer - up to 5
	"""

	def buildTree(self, treeBuilder = dict()):
		treeBuilder[self.depth] = treeBuilder.get(self.depth,[]) + [str(self.value)]
		treeBuilder = self.left.buildTree(treeBuilder = treeBuilder) if self.left != None else treeBuilder
		treeBuilder = self.right.buildTree(treeBuilder = treeBuilder) if self.right != None else treeBuilder
		return treeBuilder
		
	def lineBuilder(self,integers, spaces):
		tabs = (spaces - sum([len(str(x)) for x in integers]))/(len(integers) + 1)
		return "".join([tabs*" " + str(x) for x in integers])

	def printTree(self):
		printDict = self.buildTree()
		spaces = 88
		for depth in range(self.depth,0,-1):
			print self.lineBuilder(printDict[depth],spaces)
		return 1


if __name__ == "__main__":
	global uniqueList
	depth = 5
	uniqueList = range(pow(2,depth + 1))
	tree = BinaryTree(depth = depth)
	#nodeA,nodeB = tree.getRandomNodes(number = 2)
	#print nodeA.value
	print "==========================\n     Here's the tree!\n=========================="
	tree.printTree()
	print tree.commonParent(tree.getRandomNodes(number = 5)).value



