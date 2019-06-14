# include <stdio.h>
# include <stdlib.h>

struct ListNode
{
	int num;
	struct ListNode *next;
};

/* declaring char will be able to make a LL string; it's worth mentioning besides declaring int num we can do int *num */
/* also advanced LL could be consist of current item as struct */

void printList(struct ListNode *n) 
{ 
  while (n != NULL) 
  { 
     printf("%d ", n->num); 
     n = n-> next; 
  }
  printf("\n"); 
} 
/* traversal in LL */

void findNode(struct ListNode *n, int i) 
{ 

  if (n == NULL || i < 0)
  	printf("empty LL\n");
  else
	  while (i > 0) 
	  { 
	     n = n-> next;
	     if (n == NULL)
	     	break;
	     i--;
	  }
  printf("%d\n", n->num);
} 

int main()
{
	int n;
	struct ListNode *newNode, *head = NULL;
	scanf("%d", &n);
	if (n>0) 
	{
		newNode = malloc(sizeof(struct ListNode));
		head = newNode;
		for (int i=1; i<n; i++)
		{
			scanf("%d", &newNode->num);
			newNode->next=malloc(sizeof(struct ListNode));
			newNode=newNode->next;
		}
		scanf("%d", &newNode->num); //the last numnewNode->next=NULL;
	}
	printList(head);
	findNode(head, 3);
}