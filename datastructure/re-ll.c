# include <stdio.h>
# include <stdlib.h>

struct Node
{
	int value;
	struct Node *nextNode;
};

int traversal(struct Node *ptr)
{
	int length = 0;
	while(ptr != NULL)
	{
		printf("%d ", ptr->value);
		ptr = ptr->nextNode;
		++length;
	}
	printf("end.\n");
	return length;
}
// to add counting length func in traversal for adding or deleting node;

void traversal_Match(struct Node *ptr, int val)
{
	int counter = 1;
	while(ptr != NULL)
	{
		if (ptr->value == val)
		{
			//printf("%d\n", counter);
			break;
		}
		else
		{
			ptr = ptr->nextNode;
			++counter;
		}
		
	}
	if (ptr == NULL)
	{
		printf("val not found\n");
	}
	printf("value %d is at %d th node\n", val, counter);
}

struct Node *get_nth_node_ptr (struct Node *ptr, int nthnode)
{
	int counter = 1;
	struct Node *cur_ptr;
	while(ptr != NULL && (counter != nthnode))
	{
		++counter;
		ptr = ptr->nextNode;
	}
	printf("%d th value is %d\n", nthnode, ptr->value);
	cur_ptr = ptr;
	return cur_ptr;
}

/* no idea why this part exist 
struct Node *check_nthnode_ptr(struct Node *ptr, int nthnode)
{
	struct Node *cur_ptr;
	cur_ptr = get_nth_node_ptr(ptr, nthnode);
	printf("in check_nthnode_ptr current value %d, next value %d\n", cur_ptr->value, (cur_ptr->nextNode)->value);
	return cur_ptr;
}
*/

struct Node *add_node(struct Node *ptr, int nthnode, int insert_value, int length)
{
	if (nthnode == 1)
	{
		struct Node *nhead;
		nhead = malloc(sizeof(struct Node));
		nhead->value = insert_value;
		nhead->nextNode = ptr;
		traversal(nhead);
		return nhead;
	}
	else if (nthnode == length+1)
	{
		struct Node *tail, *last;
		tail = malloc(sizeof(struct Node));
		tail->value = insert_value;
		last = get_nth_node_ptr(ptr, length);
		last->nextNode = tail;
		traversal(ptr);
		return ptr;
	}
	else
	{
		struct Node *previous_node, *newnode, *temp;
		newnode = malloc(sizeof(struct Node));
		previous_node = get_nth_node_ptr(ptr, (nthnode-1));
		temp = previous_node->nextNode;
		previous_node->nextNode = newnode;
		newnode->value = insert_value;
		newnode->nextNode = temp;
		traversal(ptr);
		return ptr;
	}
}

struct Node *delete_node(struct Node *ptr, int nthnode, int length)
{
	if (nthnode == 1)
	{
		struct Node *cur_node, *nhead;
		cur_node = get_nth_node_ptr(ptr, nthnode);
		nhead = cur_node->nextNode;
		free(cur_node);
		free(ptr);
		traversal(nhead);
		return nhead;
	}
	else if ( nthnode == length)
	{
		struct Node *tail_node, *n_tail_node;
		n_tail_node = get_nth_node_ptr(ptr, (nthnode-1));
		tail_node = get_nth_node_ptr(ptr, nthnode);
		n_tail_node->nextNode = NULL;
		free(tail_node);
		traversal(ptr);
		return ptr;

	}
	else
	{
		struct Node *previous_node, *cur_node;
		previous_node = get_nth_node_ptr(ptr, (nthnode-1));
		cur_node = get_nth_node_ptr(ptr, nthnode);
		previous_node->nextNode = cur_node->nextNode;
		free(cur_node);
		traversal(ptr);
		return ptr;
	}
}

int main()
{
	struct Node *nNode, *head = NULL;
	struct Node *cur;
	int value, length;
	int user_input, nthnode, insert_value, nlength;
	nNode = malloc(sizeof(struct Node));
	head = nNode;
	printf("length?\n");
	scanf("%d", &length);
	printf("start:\n");
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
	// printf("1. add 2. delete 3.print all\n");
	// scanf("%d", &user_input);
	while (1)
	{
		printf("1. add 2. delete 3.print all\n");
		scanf("%d", &user_input);
		switch (user_input)
		{
			case 1:
				printf("to add to nth location? \n");
				scanf("%d", &nthnode);
				printf("value of new node? \n");
				scanf("%d", &insert_value);
				nlength = traversal(head);
				head = add_node(head, nthnode, insert_value, nlength);
				break;
			case 2:
				printf("to delete nth location? \n");
				scanf("%d", &nthnode);
				nlength = traversal(head);
				head = delete_node(head, nthnode, length);
				break;
			case 3:
				traversal(head);
				break;
			default:
				printf("please choose the correct option\n");
				break;
		}
	}
	//traversal(head);
	//traversalMatch(head, 3);
	//cur = check_nthnode_ptr(head, 4);
	//printf("in main cur value %d, nxt value %d\n", cur->value, (cur->nextNode)->value);
	//add_node(head, 3, 19, 5);
	// to resolve next call of traversal (basically make the linked-list alive until termination)
	//head = delete_node(head, 3, 5);

	return 0;
}