"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
	10 = max(10, 5, 2)
	7 = max(5, 2, 7)
	8 = max(2, 7, 8)
	8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them
"""
from itertools import combinations

a = [10, 5, 2, 7, 8, 7]
k = 3

def remove_duplicate(array):
	n_a = []

	for i in range(len(a)):
		if (a[i] not in n_a):
			n_a.append(a[i])
	return n_a
n_a = remove_duplicate(a)
n_a.sort()

# preparation takes takes linear time and space

"""
not sure if continuous k number of subarray all all combination
matters as given only length of 4 is returned but 5C3 gives 10
"""

comb = list(combinations(n_a, k))

for i in range(len(comb)):
	print(comb[i][-1])

# or

print(n_a)

for i in range((k-1), len(n_a)):
	print(n_a[k-1])
	k +=1

# both approach takes linear time to process