"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2
to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

e1
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

e2
Input: nums = [2,0,1]
Output: [0,1,2]

e3
Input: nums = [0]
Output: [0]

e4
Input: nums = [1]
Output: [1]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

Follow up:
Could you come up with a one-pass algorithm using only constant extra space?
"""


def solution(nums):
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    start = -1
    current = 0
    end = len(nums)
    while end > current:
        if nums[current] == 0:
            start += 1
            swap(start, current)
            current += 1
        elif nums[current] == 1:
            current += 1
        elif nums[current] == 2:
            end -= 1
            swap(end, current)


"""
start always lag behind thus its safe to preincrement it before swap.
we are not moving current if nums[current] == 2,
because we have see what has been swapped over
"""