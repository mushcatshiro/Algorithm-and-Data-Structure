"""
Given a string s,
return true if the s can be palindrome
after deleting at most one character from it.

e1
Input: s = "aba"
Output: true

e2
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

e3
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.

tag: two pointers
"""


def solution(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return is_palindrome(s, i + 1, j) or\
                is_palindrome(s, i, j - 1)
        else:
            i += 1
            j -= 1
    return True


def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


assert is_palindrome('abcba') is True
assert is_palindrome('ab') is False
assert is_palindrome('aa') is True
assert is_palindrome('0a') is False

assert solution('aba') is True
assert solution('abc') is False
assert solution('abca') is True
assert solution('zxxzz') is True

"""
corner case handling. sb.
"""