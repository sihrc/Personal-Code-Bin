/*
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/
#include <math.h>
#include <stdio.h>
#include <vector>

long paltoNum(std::vector<int> &array){
	long sum = 0;
	for (unsigned int i = 0; i < array.size(); i++){
		sum += array[i] * int(pow(10,i));
	}
	return sum;
}

bool isProd(long &prod1, int digits){
	std::vector<long> factors;
	long divisor = 2;
	
	while (divisor < prod1){
		if (prod1 % divisor == 0){
			factors.push_back(divisor);	
		}
		divisor++;
	}

	long factor2;
	for (long num : factors){
		if (num > pow(10,digits - 1) and num < pow(10,digits)){
			factor2 = prod1/num;
			if (factor2 > pow(10,digits - 1) and factor2 < pow(10,digits)){
				prod1 = factor2;
				return true;
			}
		}
	}
	return false;
}
		
	


int main(){
	int digits = 3;
	int curdigits = digits * 2 - 1;
	int mid;

	std::vector<int> number (curdigits + 1,9);	
	if (curdigits % 2 == 0){mid = curdigits/2;} else {mid = curdigits/2 + 1;}

	while (1){
		int index = mid;
		while (index <= curdigits){
			if (number[index] > 0){
				number[index]--;
				number[curdigits - index]--;
				break;
			}
			else{
				number[index] = 9;
				number[curdigits - index] = 9;
			}
			index += 1;
		}
		long value = paltoNum(number);
		if (isProd(value,digits)){
			printf("Palindrome found is:%ld\n",paltoNum(number));
			printf("Factor 1 found is:%ld\n",value);
			printf("Factor 2 found is:%ld\n",paltoNum(number)/value);
			return 1;
		}
	}
	return 0;
}
