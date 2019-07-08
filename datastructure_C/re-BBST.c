# include <stdio.h>
# include <stdlib.h>

// BBST easiest implementation is to sort the array then find mid_point = n/2 (+- 1 for odds) as root, recursively do for the left and right portion (as next node)

struct Node
{
	int value;
	struct Node *leftNode;
	struct Node *rightNode;
};

void traversetree(struct Node *ptr)
{
	//in order 123; pre order 213; post order 132
	if (ptr != NULL)
	{
		traversetree(ptr->leftNode);
		printf("%d ", ptr->value);
		traversetree(ptr->rightNode);
	}
}

struct Node *binary_sort(int arr[], int start, int end)
{
	if (start > end)
	{
		return NULL;
	}
	int mid = (start + end)/2;
	struct Node *root;
	root = malloc(sizeof(struct Node));
	root->value = arr[mid];
	root->leftNode = root->rightNode = NULL;
	root->leftNode = binary_sort(arr, start, mid-1);
	root->rightNode = binary_sort(arr, mid+1, end);
	return root;
}

int main()
{
	struct Node *root;
	int arr_size;
	// int arr[20] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
	int arr[21] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21};
	arr_size = sizeof(arr)/sizeof(arr[1]);
	printf("%d\n", arr_size);
	root = binary_sort(arr, 0, arr_size-1);
	traversetree(root);
	return 0;
}