//problem_2.cpp

/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*/
#include <iostream>

int main(){
	
	int sum = 2;
	int fib_1 = 1;
	int fib_2 = 2;
	int next_fib;
	int max_fib = 4000000;

	while (fib_2 < max_fib) {
		next_fib = fib_1 + fib_2;
		fib_1 = fib_2;
		fib_2 = next_fib;
		std::cout << fib_2 << " ";
		if (next_fib % 2 == 0){
			sum += next_fib;
		}
		
	}
	std::cout << sum << std::endl;
	return sum;
}