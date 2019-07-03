# include <stdio.h>
# include <stdlib.h>

// linked-list queue

struct Node
{
	int value;
	struct Node *nextNode;
};

struct Node *rear = NULL;
struct Node *front = NULL;

void peek(struct Node *front)
{
	printf("%d\n", front->value);
}

struct Node *enqueue(struct Node *rear)
{
	struct Node *nNode;
	int value;
	printf("insert value:\n");
	scanf("%d", &value);
	nNode->value = value;
	rear->nextNode = nNode;
	rear = nNode;
	return rear;
}

struct Node *dequeue(struct Node *front)
{
	struct Node *temp;
	temp = front->nextNode;
	free(front);
	front = temp;
	return front;
}

int main()
{
	struct Node *nNode;
	int length, value;
	nNode = malloc(sizeof(struct Node));
	front = nNode;
	printf("length?\n");
	scanf("%d", &length);
	printf("start:\n");
	while (length > 1)
	{
		scanf("%d", &value);
		nNode->value = value;
		nNode->nextNode = malloc(sizeof(struct Node));
		nNode = nNode->nextNode;
		rear = nNode;
		--length;
	}
	scanf("%d", &value);
	nNode->value = value;
	rear = nNode;
	peek(front);
	peek(rear);
	rear = enqueue(rear);
	front = dequeue(front);
	peek(rear);
	peek(front);
	return 0;
}