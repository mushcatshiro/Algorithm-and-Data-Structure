"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
	1, 1, 1, 1
	2, 1, 1
	1, 2, 1
	1, 1, 2
	2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time
"""

import copy

def all_ways(total_steps, lst = []):
	# recursion in action?
	if (total_steps > 0 and (total_steps - 1) >= 0):
		lst1 = copy.deepcopy(lst)
		lst1.append(1)
		all_ways((total_steps - 1), lst1)
		
	if (total_steps > 0 and (total_steps - 2) >= 0):
		lst2 = copy.deepcopy(lst)
		lst2.append(2)
		all_ways((total_steps - 2), lst2)

	if (total_steps == 0):
		print(lst)

all_ways(5)

# space complexity is not good as copies of same list is being created throughout the recursions
# time complexity should be similar to tree O(2^n) (slightly better in terms of not being a perfect tree)

# above is not the solution but act as practise to show all possible ways to climb the staircase
# limitation/improvement how to implement climb any given steps?

def no_of_ways(total_steps, steps):

	count = 0

	if (total_steps <= 1):
		return (1)

	for step in steps:
		if (total_steps-step >= 0):
			count += no_of_ways((total_steps - step), steps)
	return (count)

print(no_of_ways(5, [1,2]))

# time complexity should be O(2^n) similar to all_ways
# space complexity should be O(1)