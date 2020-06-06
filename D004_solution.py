"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place
"""

# alian SPI smallest positive integer

# lst = [3, 4, -1, 1]
# lst = [1, 2, 0, 3]
# lst = [-3, -2, -1]
lst = [-1, 0, 1]

# first approach

class solution_1:
	def __init__ (self, lst):
		self.lst = lst
	def missing_smallint (self):
		self.lst.sort()
		for index, i in enumerate(self.lst):
			print(f'index: {index}, i: {i}')
			if index == 0:
				diff = abs(index - i)
				continue
			if abs(index - i) == diff:
				continue
			else:
				print('smallest missing integer', i+1)
		print(f'no missing integer in the list thus missing item is:\
				f{(self.lst[len(lst)-1])+1}')

# T O(n)

# sol_1 = solution_1(lst)
# sol_1.missing_smallint()

# situation 1 if all -ve then 1 is the SPI
# -ve + ve continuous then largest +ve +1
# -ve + ve not continuous find in between
# +ve continuous then largest +ve +1
# not efficient

class solution_2:
	def __init__ (self, lst):
		self.lst = lst
	def missing_smallint (self):
		SPI = 1
		while SPI in set(self.lst):
			SPI += 1
		return SPI

sol_2 = solution_2(lst)
print(sol_2.missing_smallint())

# excluding search with in operator (complexity T O(n)), T O(n) else O(n^2)
# using set to remove duplicates