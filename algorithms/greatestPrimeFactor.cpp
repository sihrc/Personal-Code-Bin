
#include <stdio.h>
int main(){
	long given = 2592248347648754160;
	long divisor = 2;
	long remain = given; 
	long curLargest;

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
