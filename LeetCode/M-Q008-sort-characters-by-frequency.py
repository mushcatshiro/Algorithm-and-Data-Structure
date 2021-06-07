"""
Given a string s,
sort it in decreasing order based on the frequency of characters,
and return the sorted string.

e1
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'.
Therefore "eetr" is also a valid answer.

e2
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times,
so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect,
as the same characters must be together.

e3
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer,
but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 105
s consists of English letters and digits.

tags: bucket sort
"""


def solution(s):
    tmp = {}
    for i in s:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1
    required_buckets = max(tmp.values())
    bucket = [[] for i in range(required_buckets + 1)]
    print(bucket)
    for key, value in tmp.items():
        bucket[value].append(key)
    res = ''
    for i in range(required_buckets, 0, -1):
        if bucket[i]:
            res += ''.join([i * c for c in bucket[i]])
    return res
