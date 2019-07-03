# include <stdio.h>
# include <stdlib.h>

struct Node
{
	int value;
	struct Node *leftNode;
	struct Node *rightNode;
};

void insert_value()
{

}

int main()
{
	struct Node *root, *left = NULL, *right = NULL;
	int value;
	char input;
	printf("insert root value\n");
	scanf("%d", &value)
	root = malloc(sizeof(struct Node));
	root->value = value;
	printf("insert value?\n");
	scanf("%d", &input);
	while (input == 'y')
	{
		scanf("%d", &value);
		left, right = insert_value(value, left, right);
	}
	return 0;
}