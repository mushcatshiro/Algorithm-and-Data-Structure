"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


class solution_1:
    def __init__(self, input_integer):
        self.input_integer = input_integer

    def reverse_integer(self):
        s = ''
        while (self.input_integer != 0):
            s = s + str(self.input_integer % 10)
            self.input_integer = int(self.input_integer / 10)
            return s

# time complexity O(log(n)) due to there exists log(n) numbers in input
# space complexity O(1) assuming we are dealing with C we would know beforehand
# size of our input_integer

# we didn't address the overflow problem with solution_1


class solution_2:
    def __init__(self, input_integer, max_size, min_size=None):
        self.input_integer = input_integer
        # assumption max_size is always given
        self.max_size = max_size - 1
        self.min_size = min_size if min_size else -max_size
        self.sign = True if input_integer > 0 else False

    def reverse_integer(self) -> int:
        # one liner attempt
        if self.input_integer > self.max_size or \
           self.input_integer < self.min_size:
            return 0
        else:
            out = int(str(self.input_integer)[::-1]) if self.sign \
                else -1 * int(str((self.input_integer * -1))[::-1])

            return out


def solution_3(x: int) -> int:
    neg = True if x < 0 else False
    if neg:
        x = x * -1
    y = 0

    while x != 0:
        y = y * 10 + x % 10
        x = x // 10
    if neg:
        y = y * -1
    if y >= 2 ** 31 - 1 or y <= 2 ** 31 * - 1:
        return 0
    return y


assert solution_2(2009854, 2**32).reverse_integer() == 4589002
assert solution_2(-2009854, 2**32).reverse_integer() == -4589002
assert solution_2(2009854, 2**8).reverse_integer() == 0
assert solution_2(-2009854, 2**8).reverse_integer() == 0
