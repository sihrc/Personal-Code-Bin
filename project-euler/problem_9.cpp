/*
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
*/


#include <stdio.h>

int main()
{
	int sum = 1000;
	int a,b,c;
	b = sum/4;
	a = sum/4;

	for (c = sum/3; c != sum; c++){
		for (a = (1000 - c)/2; a != 0; a--){
			b = 1000 - a - c;
			if (a*a + b*b == c*c){
				printf("%d,%d,%d\n",a,b,c);
				printf("Prod:%d\n",a*b*c);
			}
		}
	}
	return 0;
}