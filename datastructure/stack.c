# include <stdio.h>
# include <stdlib.h>

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

int main()
{
	struct Node *nNode;
	int length, value;
	nNode = malloc(sizeof(struct Node));
	top = nNode;
	printf("length?\n");
	scanf("%d", &length);
	while (length > 1)
	{
		scanf("%d", &value);
		nNode->value = value;
		top = malloc(sizeof(struct Node));
		top->nextNode = nNode;
		nNode = top;
		--length;
	}
	scanf("%d", &value);
	nNode->value = value;
	traversal(top);
	top = add_node(top);
	top = add_node(top);
	traversal(top);
	top = delete_node(top);
	traversal(top);
	return 0;
}