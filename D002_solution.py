"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""


lst = [1, 2, 3, 4, 5]
nlst = []
llst = []
mlst = []
total = 1

# first approach

class solution_1:
	def __init__ (self, lst, total, nlst):
		self.lst = lst
		self.total = total
		self.nlst = nlst
	def arr_division (self):
		for i in self.lst:
			self.total = self.total * i
		# print(self.total)
		for i in self.lst:
			self.nlst.append(int(self.total / i))
		print(self.nlst)
# T O(n)

sol_1 = solution_1(lst, total, nlst)
sol_1.arr_division()


# second approach, no division

class solution_2:
	def __init__ (self, lst, total, llst):
		self.lst = lst
		self.total = total
		self.llst = llst
	def arr_ndivision (self):
		for i in self.lst:
			for index, j in enumerate(self.lst):
				if i == index + 1 :
					continue
				else:
					self.total = self.total * j
			self.llst.append(self.total)
			self.total = 1
		print(self.llst)

# T O(n^2)
# using llst to prevent continuation of appending sol_2 answer to nlst

sol_2 = solution_2(lst, total, llst)
sol_2.arr_ndivision()

# thrid approach, reduce redundancy of second approach?
# CIP

class solution_3:
	def __init__ (self, lst, total, mlst):
		self.lst = lst
		self.total = total
		self.mlst = mlst
	def arr_division (self):
		self.mlst = [1] * len(self.lst)
		for index, i in enumerate(self.lst):

			if i == index + 1 :
				continue
			else:
				self.total = self.total * i
		self.mlst.append(self.total)
		self.total = 1
		print(self.mlst)

# T O(n^2)
# using mlst to prevent continuation of appending sol_2 answer to nlst

sol_3 = solution_3(lst, total, mlst)
sol_3.arr_division()