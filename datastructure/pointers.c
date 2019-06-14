# include <stdio.h>

/* return can only return one value, how to update multiple values? use pointers */

int main()
{
	int num = 5
	printf("%d, %p\n", num, &num);
	/* & means the memory address of; as long as its not destroyed num always have the same address */
	int *ptrI;
	/* pointer variable, it stores the address of ptrC not the value */
	ptrI = &num;
	/* assign num to that particular address eg. memadd1234 stores value of num 5, ptrI atmemadd 2345 stores 1234*/
	*ptrI = 10
	/* update num to 10 */
	int *ptr2, *prt1;
	ptr2 = ptr1;
	/* let different memadd point to same value, original variable still exist */
}

int main2()
{
	int num1 = 3, num2 = 5; // integer variables
	int *ptr1, *ptr2; // pointer variables
	ptr1 = &num1; /* put the address of num1 into ptr1 */
	// What are the values for num1, *ptr1?, num1 = 3, *ptr1 = 3
	printf(“num1 = %d, *ptr1 = %d\n”, num1, *ptr1);
	ptr2 = &num2; /* put the address of num2 into ptr2 */
	// What are the values for num2, *ptr2?, num2 = 5, *ptr2 = 5
	printf(“num2 = %d, *ptr2 = %d\n”, num2, *ptr2);
	/* increment by 1 the content of the memory location pointed by ptr1 */
	(*ptr1)++;
	// What are the values for num1, *ptr1?, num1 = 4, *ptr1 = 4
	printf(“num1 = %d, *ptr1 = %d\n”, num1, *ptr1);
	/* copy the content of the location pointed by ptr1 into the location pointed by ptr2*/
	*ptr2 = *ptr1;
	// What are the values for num2, *ptr2?, num2 = 4, *ptr2 = 4
	printf(“num2 = %d,*ptr2 = %d\n”,num2, *ptr2);
	*ptr2 = 10; /*10 copied into the location pointed by ptr2*/
	num1 = *ptr2; /* copy the content of the memory location pointed by ptr2 into num1 */
	printf(“num1 = %d,*ptr1 = %d\n”,num1, *ptr1);
	/* num1 = 10, *ptr1 = 10*/
	*ptr1 = *ptr1 * 5;
	printf(“num1 =%d, *ptr1 = %d\n”,num1, *ptr1);
	/* num1 = 50, *ptr1 = 50*/
	ptr2 = ptr1; /*address in ptr1 copied into ptr2 */
	printf(“num2 = %d, *ptr2 = %d\n”, num2, *ptr2);
	/* num2 = 10, *ptr2 = 50*/
	return 0;
}