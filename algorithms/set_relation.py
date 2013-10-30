"""
Set Relation: Has a subset, is a subset, or none

author: Chris Lee
created: 10/12/2013
"""


def determineRelation(S1, S2):
	if len(S1) != len(set(S1)) or len(S2) != len(set(S2)):
		return "One of these isn't a set!"
	
	def subset(xs,ys):
		for element in xs:
			if element not in ys:
				return False
		return True

	if len(S1) == len(S2):
		if subset(S1,S2):
			return "S1 is equal to S2."
	else:
		if subset(S1,S2):
		 	return "S1 is a subset of S2" 
		elif subset(S2,S1):
			return "S2 is a subset of S1"
	return "No Relation"





if __name__ == "__main__":
	#Given to sets: S1, S2
	print determineRelation([1,2,3],[1,2,3])		#Equal
	print determineRelation([1,2,3,4],[1,2,3])		#S2 in S1
	print determineRelation([1,2,3],[1,2,3,4])		#S1 in S2
	print determineRelation([1,2,3,4],[10,1,2,3])	#None


