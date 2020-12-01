"""
Given a non-negative integer x,
compute and return the square root of x.

Since the return type is an integer,
the decimal digits are truncated,
and only the integer part of the result is returned.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since the decimal part is truncated, 2 is returned.
"""


class solution_1:
    def __init__(self, input_int):
        self.input_int = input_int

    def sqrt(self):
        # newton method
        guess = self.input_int
        while int(guess) * int(guess) > self.input_int:
            guess = guess - ((guess * guess - self.input_int) / (2 * guess))
        return int(guess)

    def sqrt_1(self):
        left = 1
        right = self.input_int
        print(self.input_int)
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= self.input_int:
                left = mid + 1
            else:
                right = mid - 1
            print(left, right, mid)
        return left - 1


assert solution_1(8).sqrt_1() == 2
assert solution_1(4).sqrt_1() == 2
