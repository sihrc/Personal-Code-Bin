/*
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

#include <stdio.h>

int main(){
	int max_num = 100;
	int n = max_num;
	
	long solution = 
	(3*n*n*n*n
	+  2*n*n*n
	-    3*n*n
	-      2*n)/12;

	printf("%ld\n",solution);
	return 1;
}