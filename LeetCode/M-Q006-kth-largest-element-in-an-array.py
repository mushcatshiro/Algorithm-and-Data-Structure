"""
Given an integer array nums and an integer k,
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

e1
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

e2
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
from typing import List


def solution(nums: List[int], k: int) -> int:
    stack = []

    for num in nums:
        if len(stack) < k:
            stack.append(num)
        elif any([num > i for i in stack]):
            stack.remove(min(stack))
            stack.append(num)
    return min(stack)


"""
note len(stack) < k not len(stack) <= k
"""