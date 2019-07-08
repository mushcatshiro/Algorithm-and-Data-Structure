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

struct Node *bsearch_tree(struct Node *ptr, int value, int count)
{
	if (ptr->value == value)
	{
		printf("found %d after binary search %d time(s)\n", value, count);
	}
	if ((ptr->leftNode == NULL) && (ptr->rightNode == NULL))
	{
		printf("value not in tree\n");
	}
	else if (ptr->value < value)
	{
		printf("moving to right\n");
		count = count + 1;
		bsearch_tree(ptr->rightNode, value, count);
	}
	else if (ptr->value > value)
	{
		printf("moving to left\n");
		count = count + 1;
		bsearch_tree(ptr->leftNode, value, count);
	}
}
/* became obsolete after modifying delete_node
struct Node *search_parent(struct Node *ptr, int value)
{
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
*/
struct Node *search_min(struct Node *ptr)
{
	struct Node *searchmin;
	searchmin = ptr->rightNode;
	if (searchmin->leftNode == NULL)
	{
			return searchmin;
	}
	else
	{
		searchmin = search_min(searchmin->leftNode);
	}

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
/*
void delete_node_old(struct Node *r_ptr, int value)
{
	struct Node *d_node, *parent, *min_node;
	int count = 0, min_val;
	d_node = bsearch_tree(r_ptr, value, count);
	parent = search_parent(r_ptr, value);
	// ommit base condition of delete root
	// 1st condition is to delete leaf
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
	// 2nd condition is to remove node with ONE child (regardless of grandchild number)
	else if ((d_node->leftNode == NULL && d_node->rightNode != NULL) || (d_node->leftNode != NULL && d_node->rightNode == NULL))
	{
		if ((parent->leftNode != NULL) && (parent->leftNode->value) == value)
		{
			if (d_node->leftNode != NULL)
			{
				parent->leftNode = d_node->leftNode;
				free(d_node);
			}
			else if (d_node->rightNode !=NULL)
			{
				parent->leftNode = d_node->rightNode;
				free(d_node);
			}
		}
		else if ((parent->rightNode != NULL) && (parent->rightNode->value) == value)
		{
			if (d_node->leftNode != NULL)
			{
				parent->rightNode = d_node->leftNode;
				free(d_node);
			}
			else if (d_node->rightNode !=NULL)
			{
				parent->rightNode = d_node->rightNode;
				free(d_node);
			}
		}
	}
	else
	{
		min_node = search_min(d_node);
		min_val = min_node->value;
		printf("min val %d\n", min_val);
		delete_node(r_ptr, min_val);
		d_node->value = min_val;
	}
}
*/

struct Node *delete_node(struct Node *r_ptr, int value)
{
	if (r_ptr == NULL)
	{
		printf("node %d not found\n", value);
		return NULL;
	}
	if (r_ptr->value > value)
	{
		r_ptr->leftNode = delete_node(r_ptr->leftNode, value);
	}
	else if (r_ptr->value < value)
	{
		r_ptr->rightNode = delete_node(r_ptr->rightNode, value);
	}
	else if (r_ptr->value == value)
	{
		//real shit incoming
		struct Node *temp;
		if (r_ptr->leftNode == NULL)
		{
			temp = r_ptr->rightNode;
			free(r_ptr);
			return temp;
		}
		else if (r_ptr->rightNode == NULL)
		{
			temp = r_ptr->leftNode;
			free(r_ptr);
			return temp;
		}
		else if ((r_ptr->leftNode != NULL) && (r_ptr->rightNode != NULL))
		{
			temp = search_min(r_ptr);
			r_ptr->value = temp->value;
			r_ptr->rightNode = delete_node(temp, temp->value);
		}
		return r_ptr;
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
	// bsearch_tree(root, 18, count);
	// test = search_parent(root, 2);
	// printf("%d\n", test->value);
	// delete_node(root, 2);
	// delete_node(root, 6);
	// delete_node(root, 7);
	// traversetree(root);
	// printf("\n");
	// delete_node(root, 8);
	// traversetree(root);
	// printf("\n");
	// delete_node(root, 9);
	// traversetree(root);
	// printf("\n");
	// delete_node(root, 12);
	// traversetree(root);
	// printf("\n");
	delete_node(root, 7);
	traversetree(root);
	printf("\n");
	return 0;
}