"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

# first approach
lst = [10, 15, 3, 7]
target = 17
ndic = {}

class solution_1:
	def __init__ (self, lst, target):
		self.lst = lst
		self.target = target
	def two_sum (self):
		for num_1 in self.lst:
			for num_2 in self.lst:
				if num_1 + num_2 == self.target:
					print("true since", num_1, "+", num_2, "is", self.target)

sol = solution_1(lst, target)
sol.two_sum()
# T O(n^2)

# second approach

class solution_2:
	def __init__ (self, lst, target, ndic):
		self.lst = lst
		self.target = target
		self.ndic = ndic
	def two_sum (self): 
		for num_1 in self.lst:
			if target - num_1 in self.lst:
				self.ndic[num_1] = target - num_1
		return ndic
sol_2 = solution_2(lst, target, ndic)
print(sol_2.two_sum())
# t O(n)

# online official? solutions

hash_table={}
for i in range(len(nums)):    # 先做一個hash table
    hash_table[nums[i]]=i
for i in range(len(nums)):
    if target-nums[i] in hash_table:
        if hash_table[target-nums[i]] != i:
            # to prevent returning itself ie target 10 = 5 + 5
            return [i, hash_table[target-nums[i]]]
return []

# or the one-pass solution

hash_table = {}
for i, num in enumerate(nums):
    if target - num in hash_table:
        return([hash_table[target - num], i])
        break    # 看到有人在這加了break, 理論上不會執行到, 但時間卻會比較短
    hash_table[num] = i
return([])
