# include <stdio.h>
# include <stdlib.h>

// accidentally created a BST that allows duplicated values in it which complicates the problem
// hence to simplify it
// must be revisited, to many unnecessary lines zz.....

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

struct Node *search_tree(struct Node *ptr, int value, int count)
{
	int skip = 0;
	if (ptr->value == value)
	{
		printf("found after binary search %d time(s)\n", count);
		skip = 1;
		return ptr;
	}
	if (ptr->value < value)
	{
		printf("moving to right\n");
		count = count + 1;
		printf("R count %d\n", count);
		search_tree(ptr->rightNode, value, count);
	}
	else if (ptr->value > value & skip != 1)
	{
		printf("moving to left\n");
		count = count + 1;
		printf("L count %d\n", count);
		search_tree(ptr->leftNode, value, count);
	}
}

struct Node *search_parent(struct Node *ptr, int value)
{
	// printf("L%d R%d\n", ptr->leftNode->value, ptr->rightNode->value);
	// good example of recursion, why its so important to have four return statement?
	if ((ptr->leftNode) == NULL && (ptr->rightNode) == NULL)
	{
		printf("dead end\n");
		return NULL;
	}
	if ((ptr->leftNode != NULL && (ptr->leftNode->value) == value) || (ptr->rightNode != NULL && (ptr->rightNode->value) == value))
	{
		return ptr;
	}
	if ((ptr->value) > value)
	{
		return search_parent(ptr->leftNode, value);

	}
	if ((ptr->value) < value)
	{
		return search_parent(ptr->rightNode, value);
	}

}

struct Node *search_min(struct Node *ptr)
{
	struct Node *searchmin;
	searchmin = ptr->leftNode;
	if (searchmin->leftNode != NULL)
	{
		search_min(searchmin->leftNode);
	}
	return searchmin;
}

struct Node *insert_value(struct Node *node, int value)
{
	if (node == NULL)
	{
		node = malloc(sizeof(struct Node));
		node->value = value;
		node->leftNode = node->rightNode = NULL;
		printf("inserted %d \n", node->value);
		return node;
	}
	if (node->value < value)
	{
		printf("moving to right\n");
		node->rightNode = insert_value(node->rightNode, value);
	}
	else if (node->value > value)
	{
		printf("moving to left\n");
		node->leftNode = insert_value(node->leftNode, value);
	}
	return node;
}

void delete_node(struct Node *r_ptr, int value)
{
	struct Node *d_node, *parent, *min_node;
	int count = 0, min_val;
	d_node = search_tree(r_ptr, value, count);
	parent = search_parent(r_ptr, value);
	if (d_node->leftNode == NULL && d_node->rightNode == NULL)
	{
		if ((parent->leftNode != NULL) && (parent->leftNode->value) == value)
		{
			printf("L!\n");
			parent->leftNode = NULL;
			free(d_node);
		}
		else if ((parent->rightNode != NULL) && (parent->rightNode->value) == value)
		{
			printf("R!\n");
			parent->rightNode = NULL;
			free(d_node);
		}
	}
	else if (d_node->leftNode == NULL && d_node->rightNode != NULL)
	{
		if (((parent->leftNode != NULL) && (parent->leftNode->value) == value) || (d_node->leftNode != NULL && d_node->rightNode == NULL))
		{
			printf("L!\n");
			parent->leftNode = d_node->rightNode;
			free(d_node);
		}
		else if ((parent->rightNode != NULL) && (parent->rightNode->value) == value)
		{
			printf("R!\n");
			parent->rightNode = d_node->rightNode;
			free(d_node);
		}
	}
	else
	{
		min_node = search_min(d_node);
		min_val = min_node->value;
		delete_node(min_node, min_val);
		d_node->value = min_val;
	}
}

int main()
{
	struct Node *root = NULL, *newNode, *test = NULL;
	int value, length = 19, i = 0, count = 0;
	int arr[19] = {18,19,12,7,17,6,8,10,5,3,9,16,2,0,1,4,13,14,15};
	printf("insert root value\n");
	scanf("%d", &value);
	newNode = malloc(sizeof(struct Node));
	root = newNode;
	// take note of the order the root pointer is set to the newNode, if declared before malloc
	// root != newnode, why?
	newNode->value = value;
	newNode->leftNode = newNode->rightNode = NULL;
	//printf("root value is %d\n", newNode->value);
	for (i; i<length; ++i)
	{
		//printf("inserting value to BST %d\n", arr[i]);
		insert_value(root, arr[i]);
	}
	//printf("traversing BST\n");
	// traversetree(root);
	// printf("\n");
	//search_tree(root, length, count);
	// test = search_parent(root, 2);
	// printf("%d\n", test->value);
	// delete_node(root, 2);
	// delete_node(root, 6);
	delete_node(root, 12);
	traversetree(root);
	printf("\n");
	return 0;
}