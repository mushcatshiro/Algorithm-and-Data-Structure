# include <stdio.h>
# include <string.h>
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
		// bp will be to have everything a break statement, plus if getting input of non 1 2 3 4 entire switch case will be skipped
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
	static int integer;
	float flt;
	/* as long as the execution continues the static value will not be destroyed, eg. when we run for loops flt will be destroyed everytime each loop completes, static will remember*/
}

int Cstring()
{
	// there are no string in C, only arrays of char
	// to initialize a variable to a string eg. python name = "shiro"
	char name[6];
	strcpy(name, "shiro");
	// strcpy(string1, string2); string 2 can be a variable thus adding to string1 similar to concatenating string
	name[0];
	// yield s
	printf("%s\n", name);
	fgets(name, sizeof(name), stdin);
	// takes in keyboard input of string. then what is scanf? reads number but have problem of reading end of line
	// the get around of not using scanf is to use fgets to read a line of input and sscanf to convert the text into numbers.
	//(The name sscanf stands for “string scanf”. sscanf is like scanf, but works on strings instead of the standard input.)
	void getdouble()
	{
		int value;
		char line[100];
		printf("Enter a value: ");
		fgets(line, sizeof(line), stdin);
		sscanf(line, "%d", &value);
		printf("Twice %d is %d\n", value, value * 2);
	}
}

int init_array()
{
	int row, columns;
	int product_codes[3] = {10, 972, 45};
	int matrix[row][columns];
	char name[4] = {'s','a','m','\0'};
	// whats the differnce in '' and ""?
	// char name[] = "Sam";
}

void side_effects()
{
	int size = 5;
	int result = ++size;
	// size is incremented, and then result is assigned the value of size (6). result is 6 and size is 6.
}

// one based counting problem, why programming uses zero based counting?