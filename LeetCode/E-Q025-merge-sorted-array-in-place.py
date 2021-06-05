"""
You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order,
and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.

e1

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6]
with the underlined elements coming from nums1

e2
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

e3
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1.
The 0 is only there to ensure the merge result can fit in nums1.

Constraints
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

tag: two pointers
"""


def solution(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        print(nums1)
        print(i, j, k)
        if i < 0:
            print('1')
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        elif j < 0:
            print('2')
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        elif nums1[i] > nums2[j]:
            print('3')
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            print('4')
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
    return nums1


def solution_not_accepted(nums1, m, nums2, n):
    i = 0
    j = len(nums1) - 2 + len(nums2)
    while i < j:
        if not nums2:
            break
        if nums2[0] <= nums1[i]:
            nums1.insert(i, nums2[0])
            nums2.pop(0)
        i += 1
    if nums2:
        return nums1[: m + n - len(nums2)] + nums2
    return nums1[: m + n - 1]


def solution_for_pride(arr, brr):
    if len(arr) < len(brr):
        return solution_for_pride(brr, arr)

    i = 0
    j = len(arr) - 1 + len(brr)
    try:
        while i < j:
            if brr[0] <= arr[i]:
                arr.insert(i, brr[0])
                brr.pop(0)
            else:
                i += 1
    except IndexError:
        arr += brr
    return arr


# assert solution_for_pride(
#     [1, 5, 9, 10, 15, 20],
#     [2, 3, 5, 8, 13]
# ) == [1, 2, 3, 5, 5, 8, 9, 10, 13, 15, 20]
# assert solution_for_pride(
#     [2, 3, 5, 8, 13],
#     [1, 5, 9, 10, 15, 20]
# ) == [1, 2, 3, 5, 5, 8, 9, 10, 13, 15, 20]
# assert solution_for_pride([1, 2], [3, 4]) == [1, 2, 3, 4]


# assert solution_not_accepted(
#     [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
# ) == [1, 2, 2, 3, 5, 6]
# assert solution(
#     [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
# ) == [1, 2, 2, 3, 5, 6]


# assert solution(
#     [4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3
# ) == [1, 2, 3, 4, 5, 6]

assert solution(
    [4, 5, 6, 0, 0, 0], 3, [1, 1, 1], 3
) == [1, 1, 1, 4, 5, 6]
"""
the question that i have failed to deliver.
also the inputs are modified to prove that i can actually solve anything.

modifying in place.
"""