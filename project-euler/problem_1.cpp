/*
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

*/

#include <iostream>

int main(){
	int max_num = 1000;
	int sum = 0;

	for (int i=1; i<max_num;++i){
		if (i % 3 == 0){
			sum += i;
			continue;
		} else if (i % 5 == 0){
			sum += i;
			continue;
		}
		else {
			continue;
		}
	}
	
	std::cout << "Sum is " << sum << std::endl;

	return sum;
}