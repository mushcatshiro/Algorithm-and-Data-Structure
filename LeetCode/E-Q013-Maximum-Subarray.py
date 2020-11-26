"""
Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach,
which is more subtle.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [0]
Output: 0

Example 4:
Input: nums = [-1]
Output: -1

Example 5:
Input: nums = [-2147483647]
Output: -2147483647

Constraints:
1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""


class solution_1:
    def __init__(self, input_array):
        self.input_array = input_array

    def largest_sum(self):
        if len(self.input_array) == 1:
            return self.input_array[0]
        largest_sum = float('-inf')
        for i in range(len(self.input_array)):
            temp_largest = float('-inf')
            prev_largest = self.input_array[i]
            for j in range(i + 1, len(self.input_array)):
                prev_largest = prev_largest + self.input_array[j]
                temp_largest = max(prev_largest, temp_largest)
            largest_sum = max(largest_sum, temp_largest)
        return largest_sum


class solution_2:
    def __init__(self, input_array):
        self.input_array = input_array

    def largest_sum(self):
        global_max = float('-inf')
        local_max = 0
        for x in self.input_array:
            local_max = max(x, local_max + x)
            global_max = max(global_max, local_max)
        print(global_max)
        return global_max


assert solution_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]).largest_sum() == 6
assert solution_2([1]).largest_sum() == 1
assert solution_2([0]).largest_sum() == 0
assert solution_2([-1]).largest_sum() == -1
assert solution_2([-2147483647]).largest_sum() == -2147483647
