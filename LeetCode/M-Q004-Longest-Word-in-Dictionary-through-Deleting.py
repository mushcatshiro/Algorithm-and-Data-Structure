"""
Given a string s and a string array dictionary,
return the longest string in the dictionary
that can be formed by deleting some of the given string characters.
If there is more than one possible result,
return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

e1
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"

e2
Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"

Constraints:
1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
"""


def solution(s, dictionary: list) -> str:
    longestWord = ''
    for word in dictionary:
        l1 = len(longestWord)
        l2 = len(word)
        if l1 > l2 or (l1 == l2 and longestWord < word):
            continue
        if (isSubStr(s, word)):
            longestWord = word
    return longestWord


def isSubStr(s, word):
    i = 0
    j = 0
    while i < len(s) and j < len(word):
        if s[i] == word[j]:
            j += 1
        i += 1
    return j == len(word)


assert solution('abpcplea', ["a","b","c"]) == 'a'