# include <stdio.h>
# define count 0

/*
const float varName = value;
printf("%f\n", varName);
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
	/* takes input */
	scanf("%d, %d", &num3, &num4);
	if (num3 + num4 == 11)
		printf("%d, %d\n", num4, num3);
	else
		printf("try again\n");
	/* evaluation */
	switch (num3)
	{
		case 1:
		case 2:
			printf("%d\n", num3);
			break;
		case 3:
		case 4:
			printf("%d\n", num4);
			break;
		default:
			printf("try again 2\n");
	}
	/* case evaluation */
	num3 > num4 ? printf("%d\n", num3) : printf("%d\n", num4);
	/* simpler format evaluation */
	//while (num3 > 0)
	//{
	//	printf("while loop, %d\n", num3);
	//	num3--;
	//}
	/* while loop */
	//for (; num4 > 0; num4--)
	//{
	//	printf("for loop, %d\n", num4);
	//}
	/* for loop */
	//do {
	//	printf("do while, %d\n", num4);
	//	num3--;
	//} while (num3 > 0);
	/* do while loop */
	for (; num3 > 0; num3--)
	{
		if (num3 > 1)
			printf("cont%d\n", num3 + num4);
			continue;
		printf("end.\n");
		/* else no needed */
	}
	return 0;
}

/* user defined function */
/* returntype, function name, parameters(declare type) */
/* must be declared before main() or contain within main() or function call at head */
float findmax(float x, float y)
{
	static int integer
	float flt
	/* as long as the execution continues the static value will not be destroyed, eg. when we run for loops flt will be destroyed everytime each loop completes, static will remember*/
	return void;
}