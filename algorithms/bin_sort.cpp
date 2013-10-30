//Bin Sort

#include <vector>
#include <stdio.h>
#include <string>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <chrono>

std::vector<int> bin(std::vector<int> &array, int digits){
	int bin_num;
	std::vector<int> newVector;
	for (int i = 0; i < 10; ++i){
		for (int num : array){
			bin_num = (num / int(pow(10,digits - 1))) % 10;
			if (bin_num == i){newVector.push_back(num);};
		};
	};
	return newVector;
}

int length(int number){
	int digits = 0;
	while (abs(number) > 0){
		number /= 10;
		digits += 1;
	}
	return digits;
}

int main(){
	auto t1 = std::chrono::high_resolution_clock::now();
	srand(time(NULL));
	int len = 10000;
	int max_digits, min_digits;

	std::vector<int> vector_array;

	for (int i = 0; i != len; ++i){vector_array.push_back(rand() % 1000);};

	max_digits = vector_array[0];
	max_digits = vector_array[1];

	printf("\nOriginal Array\n");
	for (int i : vector_array){
		printf("%d ", i);
		if ((i > max_digits) or (!max_digits)){max_digits = i;};
		if ((i < min_digits) or (!min_digits)){min_digits = i;};
	}; printf("\n\n");

	printf("Sorted Array\n");

	max_digits = length(max_digits);

	for (int i = 1; i < max_digits + 1; ++i){
		vector_array = bin(vector_array, i);
	};
	for (int n : vector_array){printf("%d ",n);}printf("\n\n");
	auto t2 = std::chrono::high_resolution_clock::now();
	printf("\n%ld Milliseconds\n" ,std::chrono::duration_cast<std::chrono::milliseconds>(t2-t1).count());
}