/*Fahrenheit-Celcius conversion table*/

#include <stdio.h>
main()
{
	float fahr, celsius;
	int start, stop, step;

	start = 0;
	stop = 300;
	step = 20;

	printf("Fahrenheit-Celsius table\n\n");

	fahr = start;
	while(fahr <= stop) {
		celsius = (5.0/9.0) * (fahr-32.0);
		printf("%3.0f %6.1f\n", fahr, celsius);
		fahr = fahr + step;
	}



	printf("\nCelsius-Fahrenheit table\n\n");
 

	celsius = start;
	while(celsius <= stop) {
		fahr = (celsius + 32.0) * (9.0/5.0);
		printf("%3.0f %6.0f\n", celsius, fahr);
		celsius = celsius + step;
	}

}