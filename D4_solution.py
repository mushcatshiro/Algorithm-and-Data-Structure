"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place
"""

# lst = [3, 4, -1, 1]
lst = [1, 2, 0, 3]

# first approach

class solution_1:
	def __init__ (self, lst):
		self.lst = lst
	def missing_smallint (self):
		self.lst.sort()
		try:
			for index, i in enumerate(self.lst):
				# print(i)
				if index == 0:
					diff = abs(index - i)
					continue
				if abs(index - i) == diff:
					continue
				else:
					print(i+1)
		except:
			print((self.lst[len(lst)+1])+1)

# T O(n)

sol_1 = solution_1(lst)
sol_1.missing_smallint()
