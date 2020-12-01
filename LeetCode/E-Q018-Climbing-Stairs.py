"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class solution_1:

    def climb(self, remaining_steps):
        if remaining_steps <= 1:
            return 1
        count = 0

        if remaining_steps - 1 >= 0:
            count += self.climb(remaining_steps - 1)
        if remaining_steps - 2 >= 0:
            count += self.climb(remaining_steps - 2)
        return count

    def climb_2(self, steps):
        ctr = [0 for x in range(steps + 1)]
        ctr[0], ctr[1] = 1, 1

        for i in range(2, steps + 1):
            ctr[i] = ctr[i - 1] + ctr[i - 2]
        return ctr[steps]


assert solution_1().climb_2(2) == 2
assert solution_1().climb_2(3) == 3
assert solution_1().climb_2(4) == 5
