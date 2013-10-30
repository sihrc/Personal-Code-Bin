//Generate primes using atkins sieve

#include <vector>
#include <stdio.h>
#include <math.h>

std::vector<bool> genPrimes(long max_num){
	std::vector<bool> array (max_num,false);
	long n;
	long square_check;

	array[0] = false;
	array[1] = false;
	array[2] = true;
	array[4] = false;

	for (long i = 5; i <= max_num; ++i){array[i] = false;}

	for (long x = 1; x <= long (pow(max_num,.5)); ++x){
		for (long y = 1; y <= long(pow(max_num,.5)); ++y){
			n = (4 * x * x) + (y * y);
			if (n <= max_num && (n%12==1 || n%12==5)){
				array[n] = !array[n];
			}
			n = (3 * x * x) + (y * y);
			if (n <= max_num && n%12 ==7){
				array[n] = !array[n];
			}
			n = (3 * x * x) - (y * y);
			if (x > y && n <= max_num && n%12==11){
				array[n] = !array[n];
			}
		}
	}
	for (long i = 5; i < long(sqrt(max_num)); ++i){
		for (long n = 1; n <= max_num; ++n){
			square_check = n*pow(i,2);
			if (square_check <= max_num){
				array[square_check] = false;	
			}
		}
	}
	return array;
}

int main(){
	long num = 15000;
	std::vector<bool> array = genPrimes(num);
	for (long n = 0; n <= num; ++n){printf("%ld: Prime:%s\n", n, array[n]?"True":"False");}
	return 0;
}
