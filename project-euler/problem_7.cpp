/*
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
*/



#include <stdio.h>
#include <vector>

bool checkPrime(std::vector<long> &primes, long check){
	if (check % 2 == 0 or check % 3 == 0){return false;}
	for (long prime:primes){
		if (check % prime == 0){return false;}
	}
	return true;
}


int main(){
	unsigned long want = 10001;
	std::vector<long> primes;
	long curNum = 5; 

	primes.push_back(2);
	primes.push_back(3);

	while (primes.size() != want){
		if (checkPrime(primes,curNum)){primes.push_back(curNum);}
		curNum++;
	}

	printf("Length of prime array:%ld\n",primes.size());
	printf("Prime at that index:%ld\n",primes.back());

	return 0;
}   