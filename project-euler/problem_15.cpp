 /*
Lattice paths
Problem 15

Starting in the top left corner of a 22 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 2020 grid?
*/

#include <stdio.h>

int main(){
	int size = 20;
	long routes = 2;
	for (int x = 1; x <= size; x++){
		for (int y = 1; y <= size; y++){
			if (x + 1 <= size  && y + 1 <= size){
				routes += 1;
			}
		}
	}
	printf("There are %ld routes\n",routes * 2);
}