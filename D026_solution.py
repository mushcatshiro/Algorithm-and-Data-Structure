"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass
"""

# using python list ot simulate SLL for simplicity
# the basic idea is to have two pointers e and f where e will be f + k
# when e reaches the last node, f will be right at where we can execute remove node function

SLL = [2, 5, 3, 6, 8, 1, 9, 4]

def RemoveKthLastElement(SLL, k):
	e = 1
	
	# front_ptr = SLL[f]
	# end_prt = SLL[e]

	# actual LL should be checking if ptr.next is not Null
	while e  != len(SLL):
		e += 1
		f = e - k + 1

	# clarify on the confussing + 1 - 1 notation, len(SLL) = 8, last kth element is 5 thus the + 1, python list counts from 0 thus the - 1
	# if its actual SLL no + 1 - 1 confussion as we need f to be pointing to the 4th node to remove the 5th/kth node from SLL

	print(len(SLL), e, f)
	SLL.pop(f - 1)
	print(SLL)
	return SLL

RemoveKthLastElement(SLL, 4)


