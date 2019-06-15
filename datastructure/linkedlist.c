# include <stdio.h>
# include <stdlib.h>

struct ListNode
{
	int num;
	struct ListNode *next;
};

/* declaring char will be able to make a LL string; it's worth mentioning besides declaring int num we can do int *num */
/* also advanced LL could be consist of current item as struct */

void printList(struct ListNode *ptr) 
{
	while (ptr != NULL) 
	// check if head pointer is pointing to NULL i.e. linked list do not exist
	{ 
		printf("%d ", ptr->num);
		// print num from address pointed from head
		ptr = ptr -> next;
		// move the pointer to the 1st node next pointer
	}
	printf("\n"); 
} 
/* traversal in LL */

struct ListNode *findNode(struct ListNode *head, int i)
{ 
	struct ListNode *cur = head;
	// make current pointer to head pointer
	if (head == NULL || i < 0)
	// check if head pointer is pointing to nothing
		printf("empty LL\n");
	else
	// if 1 = 0 skip while
		while (i > 0) 
		{
			cur = cur-> next;
			if (cur == NULL)
			break;
			i--;
		}
	printf("%d\n", cur->num);
	// if i = 0, straight print the num pointed by head pointer else run while loop ensure the *struct.next is pointing to null thus print the (*struct).num
	return cur;
	// return current pointer
}

void insertNode(struct ListNode **ptrHead, int index, int value)
{
	struct ListNode *cur, *newNode;
	// If empty list or inserting first node, need to update head pointer
	if (*ptrHead == NULL || index == 0)
	{
		newNode = malloc(sizeof(struct ListNode));
		newNode->num = value;
		newNode->next = *ptrHead;
		*ptrHead = newNode; 
	}
	// Find the nodes before and at the target position
	// Create a new node and reconnect the links
	else if ((cur = findNode(*ptrHead, index-1)) != NULL)
	{
		newNode = malloc(sizeof(struct ListNode));
		newNode->num = value;
		newNode->next = cur->next;
		cur->next = newNode; 
	}
	else 
		printf("can not insert the new item at index %d!\n", index);
}

void removeNode(struct ListNode *head, int index)
{
	struct ListNode * cur, *prev, *next;
	// get the node index to remove
	cur = findNode(head, index-1);
	prev = findNode(head, index-2);
	next = findNode(head, index);
	if (cur == NULL || index < 0)
	{
		printf("empty list\n");
	}
	else if (next == NULL)
	{
		prev = NULL;
		free(next);
	}
	// else if (prev == )
	// {
	// 	;
	// }
	else
	{
		prev->next = cur->next;
		free(cur);
	}

}

int main()
{
	int n;
	struct ListNode *newNode, *head = NULL;
	// request for newNode and head pointers
	scanf("%d", &n);
	if (n>0) 
	{
		newNode = malloc(sizeof(struct ListNode));
		// malloc allocates the requested memory and returns a pointer to it
		head = newNode;
		// make head the pointer to the first ListNode
		for (int i=1; i<n; i++)
		{
			scanf("%d", &newNode->num);
			// store the integer input to the address of (*newNode).num
			newNode->next = malloc(sizeof(struct ListNode));
			// store a new pointer to subsequent node to (*newNode).next
			newNode = newNode->next;
			// update newNode the new pointer
		}
		scanf("%d", &newNode->num); //the last numnewNode->next=NULL;
	}
	printList(head);
	findNode(head, 0);
	// printf("add node?\n");
	// scanf("%d", )
}

/*
When should you use the heap, and when should you use the stack? 
If you need to allocate a large block of memory (e.g. a large array, or a big struct), and you need to keep that variable around a long time (like a global), then you should allocate it on the heap. 
declare it global? dynamically.
If you are dealing with relatively small variables that only need to persist as long as the function using them is alive, then you should use the stack, it's easier and faster. 
however if you try to allocate too many temporary variables, you will get a “Stack overflow” error
If you need variables like arrays and structs that can change size dynamically (e.g. arrays that can grow or shrink as needed) then you will likely need to allocate them on the heap, 
and use dynamic memory allocation functions like malloc(), calloc(), realloc() and free() to manage that memory "by hand". 
*/