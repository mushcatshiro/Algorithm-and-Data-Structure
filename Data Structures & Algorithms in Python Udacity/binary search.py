"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    mid = int(len(input_array)/2)
    if ((mid == 0) and (input_array[mid] == value)):
        return input_array[mid]
    elif ((mid == 0) and (input_array[mid] != value)):
        return -1
    if (input_array[mid] > value):
        return binary_search((input_array[:mid]), value)
    elif (input_array[(mid)] < value):
        return binary_search(input_array[mid+1:], value)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)