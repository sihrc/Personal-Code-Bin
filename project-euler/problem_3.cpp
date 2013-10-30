/*
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/

#include <stdio.h>
int main(){
	long given = 2592248347648754160;
	long divisor = 2;
	long remain = given; 
	long curLargest;

	printf("\nFinding the Greatest Prime Factor of %ld\n\n", given);
	while (remain >= divisor){
		while (remain % divisor == 0){
			printf("Divisor,%ld  ",divisor);
			printf("Remain,%ld\n",remain);
			curLargest = divisor;
			remain /= divisor;
		}
		divisor += 1;
	}
	printf("%ld\n", curLargest);
	return 0;
}