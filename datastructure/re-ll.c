# include <stdio.h>
# include <stdlib.h>

struct Node
{
	int value;
	struct Node *nextNode;
};

void traversal(struct Node *ptr)
{
	while(ptr != NULL)
	{
		printf("%d\n", ptr->value);
		ptr = ptr->nextNode;
	}
	printf("end.\n");
}

void traversalMatch(struct Node *ptr, int val)
{
	int counter = 1;
	while(ptr != NULL)
	{
		if (ptr->value == val)
		{
			break;
		}
		else
		{
			ptr = ptr->nextNode;
			++counter;
		}
		
	}
	printf("value %d is at %d th node\n", val, counter);
}

struct Node *check2ptr(struct Node *ptr)
{
	return ptr, ptr->nextNode;
}


int main()
{
	struct Node *nNode, *head = NULL;
	int value, length;
	nNode = malloc(sizeof(struct Node));
	head = nNode;
	printf("length?\n");
	scanf("%d", &length);
	printf("start:");
	while (length > 1)
	{
		scanf("%d", &value);
		nNode->value = value;
		nNode->nextNode = malloc(sizeof(struct Node));
		nNode = nNode->nextNode;
		--length;
	}
	scanf("%d", &value);
	nNode->value = value;
	// why ommision of this line will result end node with value 0?
	printf("LL input complete!\n");
	//traversal(head);
	traversalMatch(head, 18);
	return 0;
}