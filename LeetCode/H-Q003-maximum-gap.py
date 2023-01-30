"""
Given an integer array nums,
return the maximum difference
between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs
in linear time and uses linear extra space

e1
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9],
either (3,6) or (6,9) has the maximum difference 3.

e2
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements,
therefore return 0.

tags: bucket sort
"""
from typing import List

def solution(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    
    min_num = min(nums)
    max_num = max(nums)
    if min_num == max_num:
        return 0
    interval = math.ceil((max_num - min_num)/(len(nums) - 1))
    buckets = [[None, None] for _ in range((max_num - min_num)//interval + 1)]
    
    for num in nums:
        bucket = buckets[(num - min_num)//interval]
        bucket[0] = min(bucket[0], num) if bucket[0] else num
        bucket[1] = max(bucket[1], num) if bucket[1] else num
    buckets = [b for b in buckets if b[0]] # removing empty buckets
    return max([buckets[i][0] - buckets[i-1][1] for i in range(1, len(buckets))])