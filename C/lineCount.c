/*This program counts the number of lines and prints the result*/

#include <stdio.h>
main(){
	int c, b, t, nl;
	nl = 0 ;
	while(getchar() != EOF){
		if (c == '\n')
			++nl;
		if (c == '\t')
			++t;
		if (c == space)
			++b;
	}
	printf("%d\n %d\n %d\n", nl, t, b);
	}	
