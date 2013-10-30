"""
Searching Sums in Binary Trees
author: Chris Lee
created: 10/13/2013
"""
import binary_tree

def findSums(value, node, path = []):
	sums = sum(path)
	if sums > value:
		del(path[0])
	path.append(node.value)
	if sums == value:
		print path
		return True
	if node.left:
		findSums(value, node.left, path = path)
	if node.right:
		findSums(value, node.right, path = path)

		



if __name__ == "__main__":
	depth = 3
	binary_tree.uniqueList = range(pow(2,depth + 1))
	tree = binary_tree.BinaryTree(depth = depth)
	#tree.printTree();
	print findSums(value = 10, node = tree, path = [])
	