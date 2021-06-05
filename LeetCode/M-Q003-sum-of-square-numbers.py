"""
Given a non-negative integer c,
decide whether there're two integers a and b
such that a ** 2 + b **2 = c.

e1
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

e2
Input: c = 3
Output: false

e3
Input: c = 4
Output: true

e4
Input: c = 2
Output: true

e5
Input: c = 1
Output: true

Constraints:
0 <= c <= 231 - 1


tag: two pointers
"""


def solution(c: int) -> bool:
    import math

    i = 0
    j = int(math.sqrt(c))

    while i <= j:
        res = i ** 2 + j ** 2
        if res == c:
            return True
        elif res > c:
            j -= i
        else:
            i += 1
    return False


assert solution(5) is True
assert solution(3) is False
assert solution(4) is True
assert solution(2) is True
assert solution(1) is True