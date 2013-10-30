if __name__ == "__main__":
	correct = []
	check = []
	
	with open("prime_output.txt",'rb') as f:
		for line in f:
			check += line.split()
		check = map(int,check)
	
	with open("primesdownload.txt",'rb') as f:
		for line in f:
			correct += line.split()
		correct = map (int, correct)

"""	
	for i in range(len(check)):
		print check[i], correct[i]
		if check[i] != correct[i]:
			raw_input()
"""
sum = 0
for num in correct:
	if num <= 2000000:
		sum += num
	else
		break
print sum

	

	