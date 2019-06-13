# include <stdio.h>
# define Tax_rate 0.12
/*
const float varName = value;
printf("%f\n", varName);

int count = 0;
*/
int main()
{
	int num1 = 1, num2 = 2;
	printf("%d + %d = %d\n", num1, num2, num1+num2);
	/* basic printing*/
	int integer = 10;
	float flt = 10.3;
	double dbl = 100.1234;
	printf("%d, %f, %f\n", integer, flt, dbl);
	/* different variables printing*/
	scanf("\n");
	int num3, num4;
	printf("input two integer\n");
	/* takes in a */
	scanf("%d, %d", &num3, &num4);
	if (num3 + num4 == 11)
		printf("%d, %d\n", num4, num3);
	else
		printf("try again\n");
	return 0;
}