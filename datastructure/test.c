# include <stdio.h>
# define dev(num) (!(num % 10)) // macro

const int count = 0;
/*
struct bin
{
	int index;
} tbin = {
	90
};
//pre init
int afunc()
{
	return count;
}

int main()
{
	int count;
	count --;
	printf("%d\n", count);
	printf("%d\n", afunc());
	printf("%d\n", dev(10));
	printf("%d\n", dev(count));
	printf("%d\n", tbin.index);
	struct bin bbin = { 30 };
	printf("%d\n", bbin.index);
	// post init
}

// -1 and 0 
// 1 and 0
*/

int main()
{
	int i, j;
	i, j = 1, 2;
	printf("%d & %d\n", i, j);
	return 0;

}