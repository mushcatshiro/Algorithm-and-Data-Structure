"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space
"""

class node:
	def __init__(self, value):
		self.value = value
		self.next = None

class sLL:

	def __init__(self, root):
		self.root = root

	def add_node(self, node):
		current = self.root
		if (self.root):
			while (current.next):
				current = current.next
			current.next = node
		else:
			self.root = node
		return(self.root)

	def traversal(self):
		current = self.root

		while (current):
			print(current.value)
			current = current.next

a = [3, 7, 8, 10]
b = [99, 1, 8, 10]

for n, element in enumerate(a):
	if (n == 0):
		LL1 = sLL(node(element))
	else:
		A = LL1.add_node(node(element))

for n, element in enumerate(b):
	if (n == 0):
		LL2 = sLL(node(element))
	else:
		B = LL2.add_node(node(element))

position = 1

while (A.value != B.value):
	A = A.next
	B = B.next
	position += 1

print(position)

# the way sLL is setup ensure list are non cyclical
# in python we can only assume nodes with same value are the exact same node obj
# constant space is fullfilled as the search only takes O(2), 3 if counted the counter
# linear (sum) time should be fullfilled assuming A and B have same length, the same value exists at the same position (eg. if 8 is changed to other value counter output will be 4), thus O(M+N) is satisfied where M+N = 2N
