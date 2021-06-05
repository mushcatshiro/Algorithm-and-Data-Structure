"""
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

e1
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

e2
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

tag: two pointers
"""

def solution(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if helper(s[i], s[j]):
            return False
        else:
            i += 1
            j -= 1
    return True

def helper(c1, c2):
    return c1.lower() != c2.lower()


"""
one of the more tricker question on boundary. sb.
"""