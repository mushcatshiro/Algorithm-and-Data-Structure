# include <stdio.h>
# include <stdlib.h>

// to revisit this problem

struct Node
{
	int value;
	struct Node *nextNode;
}*top;

void traversal(struct Node *top)
{
	printf("your stack is: ");
	while(top != NULL)
	{
		printf("%d ", top->value);
		top = top->nextNode;
	}
	printf("end.\n");
}
/*
struct Node *add_node(struct Node *top)
{
	struct Node *nNode;
	int value;
	printf("value to insert to new node?\n");
	scanf("%d", &value);
	nNode = malloc(sizeof(struct Node));
	nNode->value = value;
	nNode->nextNode = top;
	top = nNode;
	return top;
}

struct Node *delete_node(struct Node *top)
{
	struct Node *ntop;
	ntop = top->nextNode;
	free(top);
	top = ntop;
	return top;
}
*/
struct Node *create_tower(int disk)
{
	struct Node *nNode;
	nNode = malloc(sizeof(struct Node));
	top = nNode;
	while (disk > 1)
	{
		nNode->value = disk;
		top = malloc(sizeof(struct Node));
		top->nextNode = nNode;
		nNode = top;
		--disk;
	}
	nNode->value = disk;
	return top;
}

int main()
{
	struct Node *A, *B, *C;
	int disk =5;
	A = create_tower(disk);
	traversal(A);
	return 0;
}