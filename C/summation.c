/*This program sums the integers from 20 to 30 */

#include <stdio.h> 
#define LOWER 20
#define UPPER 30
#define STEP 1
main(){
	
	int count = 0;
 	int sum = LOWER;
 	while (sum < UPPER){
 		sum = sum + count ;
 		count = count + STEP ;
 	}
 	printf("%3d\n", sum);
}
		 
		

