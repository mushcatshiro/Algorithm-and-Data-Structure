"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
l = ['quick', 'brown', 'the', 'fox']
s = "thequickbrownfox"

# solution seems to be easy in python

r = []

for i in range(len(l)):
	if (l[i] in s):
		r.append(l[i])

print(r)

# problem how to follow the given string order?

# better solution
# time complexity is O(n!/(n-k)!), given n = k thus O(n!)
# space complexity is O(n!/(n-k)!), given n = k thus O(n!)

import itertools as it

def attempt_2(l, s):
	all_combinations = [i for i in it.permutations(l)]
	for i in all_combinations:
		if ''.join(i) == s:
			return i

solution = attempt_2(l, s)