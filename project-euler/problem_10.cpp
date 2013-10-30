/*
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/

#include <stdio.h>
#include <vector>
#include <math.h>

long int sumPrimes(std::vector<bool> &primes, long limit){
	primes[0] = false;
	primes[1] = false;
	primes[2] = true;
	primes[3] = true;

	long int sqrtlimit = sqrt(limit);
	long int n;
	long int sum = 0;

	for (long int x = 1; x <= sqrtlimit; ++x){
		for (long int y = 1; y <= sqrtlimit; ++y){
			n = 4 * x * x + y * y;
			if (n <= limit && (n%12 == 1 || n%12 == 5))
				{primes[n] = !primes[n];}
			n = 3 * x * x + y * y;
			if (n <= limit && n%12 == 7)
				{primes[n] = !primes[n];}
			n = 3 * x * x - y * y;
			if (x > y && n <= limit && n%12==11)
				{primes[n] = !primes[n];}
		}
	}

	for (long int n = 5; n <= sqrtlimit; n++){
		if (primes[n]){
			long int counter = 1;
			while (counter * n * n <= limit){
				primes[counter * n * n] = false;
				counter++;
			}
		}
	}

	for (long int n = 0; n < primes.size(); n++){
		if (primes[n]){sum += n;}
	}

	return sum;
}

int main()
{
	long limit = 2000000;
	std::vector<bool> primes (limit,false);
	printf("Sum of primes up to %ld is %ld.\n",limit,sumPrimes(primes,limit));
	return 0;
}