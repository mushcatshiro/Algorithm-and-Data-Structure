"""
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that 
the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which,
together with the x-axis forms a container,
such that the container contains the most water.

Notice that you may not slant the container.

e1
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by
array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water the container can contain is 49.

e2
Input: height = [1,1]
Output: 1

e3
Input: height = [4,3,2,1,4]
Output: 16

e4
Input: height = [1,2,1]
Output: 2

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104

tag: two pointers
"""


def solution_slow(height: list) -> int:
    max_water = 0
    i = 0
    while i <= len(height) - 1:
        j = i + 1
        while j <= len(height) - 1:
            h1 = height[i]
            h2 = height[j]
            water = min(h1, h2) * (i - j)
            if water < 0:
                water = water * -1
            max_water = max(water, max_water)
            j += 1
        i += 1
    # print(max_water)
    return max_water


def solution(height: list) -> int:
    i = 0
    j = len(height) - 1
    max_water = 0
    while i < j:
        water = min(height[i], height[j]) * (j - i)
        if water < 0:
            water = water * -1
        max_water = max(max_water, water)
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return max_water


assert solution([1,8,6,2,5,4,8,3,7]) == 49