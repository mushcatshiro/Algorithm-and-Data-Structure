"""
Given a string s,
find the length of the longest substring without repeating characters.

e1
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

e2
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

e3
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.

e4
Input: s = ""
Output: 0

e4
Input: s = " "
Output: 1

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def distinct_helper(substring):
    tmp = {}
    for char in substring:
        if char not in tmp:
            tmp[char] = 1
        else:
            tmp[char] += 1
    return True if max(tmp.values()) == 1 else False


def solution(s):
    if len(s) == 0:
        return 0

    i = 0
    j = 1
    max_len = 0
    while j <= len(s):
        print(i, j)
        if distinct_helper(s[i: j]):
            max_len = max(max_len, (j - i))
            j += 1
        else:
            i += 1
    print(max_len)
    return max_len


assert distinct_helper('abc') == True
assert distinct_helper('abb') == False

solution('abcabcbb')
solution(' ')