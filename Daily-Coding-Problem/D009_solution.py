"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""

class Solution1(object):
    """docstring for Solution1"""
    def __init__(self, num_list):
        self.num_list = num_list

    def max_sum(self):
        incl = 0
        excl = 0

        for i in self.num_list:
            print(f'i: {i}, incl: {incl}, excl: {excl}')
            new_excl = max(excl, incl)

            incl = excl + i
            excl = new_excl
            print(f'incl: {incl}, excl: {excl}')

        return max(excl, incl)

l = [5, 1, 1, 5]
# l = [2, 4, 6, 2, 5]

q = Solution1(l)

print(q.max_sum())