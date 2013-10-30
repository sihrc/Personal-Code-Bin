#include <stdio.h>

long gcf(long a, long b){
	//UNUSED
	long divisor = 2;
	long greatest = 1;
	while (divisor <= a and divisor <= b){
		while (a % divisor == 0 and b % divisor == 0){
			//printf("a: %ld, b: %ld, greatest: %ld, divisor:%ld\n",a, b, greatest,divisor);
			greatest *= divisor;
			a /= divisor;
			b /= divisor;
		}
		divisor++;
	}

	return greatest;
}