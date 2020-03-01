"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water
"""

l_1 = [2, 1, 2]
l_2 = [3, 0, 1, 3, 0, 5]
l_3 = [2, 3, 4, 1, 0, 8, 9, 6, 5]

def waterVolume(l):
	if len(l) > 2:
		l = sorted(l, reverse=True)
		f = l[0]
		e = l[1]
		remaining = l[2:]
		vol = int(l[1]) * len(remaining)
		for i in remaining:
			vol = vol - i
		print(vol)


waterVolume(l_3)