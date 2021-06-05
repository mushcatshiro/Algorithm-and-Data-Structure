"""
Given an array of integers nums and an integer target,
return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(arr, target):
    tmp = {}
    for i, num in enumerate(arr):
        if target - num in tmp:
            return [i, tmp[target - num]]
        tmp[num] = i
    return ([])


assert set(two_sum([2, 7, 11, 15], 9)) == set([0, 1])
assert set(two_sum([3, 2, 4], 6)) == set([1, 2])