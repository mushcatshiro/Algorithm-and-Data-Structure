# include <stdio.h>
# include <stdlib.h>

// accidentally created a BST that allows duplicated values in it which complicates the problem
// hence to simplify it

struct Node
{
	int value;
	struct Node *leftNode;
	struct Node *rightNode;
};

void traversetree(struct Node *ptr )
{
	//in order 123; pre order 213; post order 132
	if (ptr != NULL)
	{
		traversetree(ptr->leftNode);
		printf("%d ", ptr->value);
		traversetree(ptr->rightNode);
	}
}

void search_tree(struct Node *ptr, int value, int count)
{
	int skip = 0;
	if (ptr->value == value)
	{
		printf("found after binary search %d time(s)\n", count);
		skip = 1;
	}
	if (ptr->value < value)
	{
		printf("moving to right\n");
		count = count + 1;
		printf("R count %d\n", count);
		search_tree(ptr->rightNode, value, count);
	}
	else if (ptr->value >= value & skip != 1)
	{
		printf("moving to left\n");
		count = count + 1;
		printf("L count %d\n", count);
		search_tree(ptr->leftNode, value, count);
	}
}

struct Node *insert_value(struct Node *node, int value)
{
	if (node == NULL)
	{
		// struct Node *nNode;
		node = malloc(sizeof(struct Node));
		// nNode = node;
		node->value = value;
		node->leftNode = node->rightNode = NULL;
		printf("inserted %d \n", node->value);
		return node;
	}
	if (node->value <= value)
	{
		// struct Node *rnode;
		// node->rightNode = malloc(sizeof(struct Node));
		// node->rightNode = rnode;
		printf("moving to right\n");
		node->rightNode = insert_value(node->rightNode, value);
	}
	else if (node->value > value)
	{
		// struct Node *lnode;
		// node->leftNode = malloc(sizeof(struct Node));
		// node->rightNode = lnode;
		printf("moving to left\n");
		node->leftNode = insert_value(node->leftNode, value);
	}
	return node;
}

void delete_node(struct Node *ptr, int level, int value)
{
	if (level == 1)
	{
		char subtree;
		printf("keep left subtree or right subtree?\n");
		scanf("%s", &subtree);
		if (subtree == 'l')
		{
			struct Node *
			free();
		}
		else
		{
			free();
		}
	}
}

int main()
{
	struct Node *root = NULL, *newNode;
	int value, length = 9, i = 0, count = 0;
	int arr[9] = {7,4,8,2,5,7,9,4,5};
	// char input;
	printf("insert root value\n");
	scanf("%d", &value);
	newNode = malloc(sizeof(struct Node));
	root = newNode;
	// take note of the order the root pointer is set to the newNode, if declared before malloc
	// root != newnode, why?
	newNode->value = value;
	newNode->leftNode = newNode->rightNode = NULL;
	printf("root value is %d\n", newNode->value);
	// printf("root ptr value is %d\n", root->value);
	// do
	// {
	// 	printf("add nodes?\n");
	// 	scanf("%s", &input);
	// 	insert_value(root)

	// }while (input == 'y');
	for (i; i<length; ++i)
	{
		printf("inserting value to BST %d\n", arr[i]);
		insert_value(root, arr[i]);
	}
	printf("before traversing BST\n");
	traversetree(root);
	printf("\n");
	search_tree(root, length, count);
	return 0;
}