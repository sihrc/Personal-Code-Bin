
//Generate primes using atkins sieve.
void genPrimes(std::vector<bool>& array, long max_num){
	
	long n;
	long square_check;

	array[0] = false;
	array[1] = false;
	array[2] = true;
	array[4] = false;

	for (long i = 5; i <= max_num; ++i){array[i] = false;}

	for (long x = 1; x <= long (pow(max_num,.5)); ++x){
		printf("%ld\n",x);
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
}
