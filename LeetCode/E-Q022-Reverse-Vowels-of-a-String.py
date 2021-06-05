"""
Given a string s,
reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both cases.

e1
Input: s = "hello"
Output: "holle"

e2
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

tag: two pointers
"""

def solution(s):
    if len(s) <= 1:
        return s

    i = 0
    j = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(s)

    while i <= j and j >= 0:
        if s[i].lower() in vowels and s[j].lower() in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        if s[i].lower() not in vowels:
            i += 1
        if s[j].lower() not in vowels:
            j -= 1
    return ''.join(s)


assert solution("hello") == "holle"
assert solution("leetcode") == "leotcede"
assert solution("Euston saw I was not Sue.") == "euston saw I was not SuE."

"""
comment:
this is the kind of question to clarify boundary,
else it will be just like shooting in your own foot when trying to debug
"""