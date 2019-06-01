"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

# first approach
lst = [1, 2, 3, 4, 5]
nlst = []
total = 1

class solution_1:
	def __init__ (self, lst, total, nlst):
		self.lst = lst
		self.total = total
		self.nlst = nlst
	def arr_division (self):
		for i in self.lst:
			self.total = self.total * i
		print(self.total)
		for i in self.lst:
			self.nlst.append(int(self.total / i))
		print(self.nlst)
# T O(n)

sol_1 = solution_1(lst, total, nlst)
sol_1.arr_division()


# second approach

class solution_2:
	def __init__ (self, lst, total, nlst):
		self.lst = lst
		self.total = total
		self.nlst = nlst
	def arr_division (self):
		for i in self.lst:
			self.total = self.total * i
		print(self.total)
		for i in self.lst:
			self.nlst.append(int(self.total / i))
		print(self.nlst)
# T O(n)

sol_2 = solution_2(lst, total, nlst)
sol_2.arr_division()