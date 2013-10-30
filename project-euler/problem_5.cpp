/*
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <stdio.h>
#include <vector>

int main(){
	long range(20);
	long divisor, curNum;

	std::vector<long> divisors;
	divisors.push_back(1);

	for (long index = 1; index <= range; index++){
		curNum = index;
		for (long cursor:divisors){
			if (curNum % cursor == 0){
			curNum /= cursor;}
		}
		printf("Adding curNum:%ld\n",curNum);
		divisors.push_back(curNum);
	}

		
	
	long sum(1);
	printf("For numbers within range of %ld, the LCM (least common multiple) of all of them is:\n", range);
	printf("Product of: ");for (long num : divisors){printf("%ld ",num);sum*=num;}
	printf(":%ld\n",sum);
	return 1;
}



