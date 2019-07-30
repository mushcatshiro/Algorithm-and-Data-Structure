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

	def add_node(self, value):
		while root.next != None:
			self.add_node(value)
