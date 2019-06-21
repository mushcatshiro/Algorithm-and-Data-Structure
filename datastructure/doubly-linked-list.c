# include <stdio.h>
# include <stdlib.h>

// i believe that singly and doubly linked list is extremely similar, just some implementation details
// thus i will only show one major difference that i think is worth mentioning

struct Node
{
	int value;
	struct Node *nextNode;
	struct Node *prevNode;
};

int traversal(struct Node *ptr, char c)
{
	int length = 0;
	if (c == 'h')
	{
		while (ptr != NULL)
		{
			printf("%d ", ptr->value);
			ptr = ptr->nextNode;
			++length;
		}
	}
	else if (c =='t')
	{
		while (ptr != NULL)
		{
			printf("%d ", ptr->value);
			ptr = ptr->prevNode;
			++length;
		}
	}
	printf("end.\n");
	return length;
}

struct Node *delete_node(struct Node *h_ptr, struct Node *t_ptr, int nthnode, int length)
{
	if (nthnode == 1)
	{
		struct Node *nhead;
		nhead = h_ptr->nextNode;
		(h_ptr->nextNode)->prevNode = NULL;
		free(h_ptr);
		return nhead;
	}
	else if (nthnode == length)
	{
		struct Node *ntail;
		ntail = t_ptr->prevNode;
		(t_ptr->prevNode)->nextNode = NULL;
		return ntail;
	}
}

int main()
{
	struct Node *nNode, *head = NULL, *tail = NULL;
	int value, length;
	nNode = malloc(sizeof(struct Node));
	head = nNode;
	printf("length? ");
	scanf("%d", &length);
	printf("start:\n");
	while (length > 1)
	{
		scanf("%d", &value);
		nNode->value = value;
		nNode->prevNode = tail;
		tail = nNode;
		nNode->nextNode = malloc(sizeof(struct Node));
		nNode = nNode->nextNode;
		--length;
	}
	scanf("%d", &value);
	nNode->value = value;
	nNode->prevNode = tail;
	tail = nNode;
	printf("doubly LL input complete!\n");
	traversal(head, 'h');
	traversal(tail, 't');
	head = delete_node(head, tail, 1, 5);
	tail = delete_node(head, tail, 5, 5);
	traversal(head, 'h');
	traversal(tail, 't');
	return 0;
}