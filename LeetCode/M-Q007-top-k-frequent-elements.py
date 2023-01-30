"""
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.

e1
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

e2
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

tags: bucket sort
"""


def solution(nums: list, k: int) -> list:
    tmp = {}
    for num in nums:
        if num not in tmp:
            tmp[num] = 1
        else:
            tmp[num] += 1
    required_buckets = max(tmp.values())
    bucket = [[] for i in range(required_buckets + 1)]
    for key, value in tmp.items():
        bucket[value].append(key)
    output = []
    for i in range(required_buckets, 0, -1):
        if bucket[i]:
            output += bucket[i]
        if len(output) >= k:
            return output[: k]


assert set(solution([4, 4, 4, 5, 5, 6], 2)) == set([4, 5])
assert set(solution([-1, -1], 1)) == set([-1])
assert set(solution([1], 1)) == set([1])
assert set(solution([1, 2], 2)) == set([1, 2])

"""
no savings on bucket creation, create them all + 1.
each bucket might have more than element thus concatenate lists instead.
"""