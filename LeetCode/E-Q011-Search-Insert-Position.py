"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


# exhaustive
class solution_1:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def search_insert_position(self):
        if self.target < self.nums[0]:
            return 0
        for i in range(len(self.nums)):
            if self.nums[i] >= self.target:
                return i
        return len(self.nums)


# python native
class solution_2:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def search_insert_position(self):
        temp = self.nums + [self.target]
        temp = sorted(temp)
        return temp.index(self.target)


# bin search
class solution_3:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def search_insert_position(self):
        start = 0
        end = len(self.nums) - 1
        mid = 0
        print(f'target: {self.target}')
        while start <= end:
            mid = (start + end) // 2
            print(f'mid: {mid}, start: {start}, end: {end}')
            if self.nums[mid] == self.target:
                return mid
            elif self.nums[mid] > self.target:
                end = mid - 1
            elif self.nums[mid] < self.target:
                start = mid + 1
        return start


assert solution_3([1, 3, 5, 6], 5).search_insert_position() == 2
assert solution_3([1, 3, 5, 6], 2).search_insert_position() == 1
assert solution_3([1, 3, 5, 6], 7).search_insert_position() == 4
assert solution_3([1, 3, 5, 6], 0).search_insert_position() == 0
assert solution_3([1], 0).search_insert_position() == 0

"""
target: 5
mid: 1, start: 0, end: 3
mid: 2, start: 2, end: 3

target: 2
mid: 1, start: 0, end: 3
mid: 0, start: 0, end: 0

target: 7
mid: 1, start: 0, end: 3
mid: 2, start: 2, end: 3
mid: 3, start: 3, end: 3

target: 0
mid: 1, start: 0, end: 3
mid: 0, start: 0, end: 0

target: 0
mid: 0, start: 0, end: 0
"""
