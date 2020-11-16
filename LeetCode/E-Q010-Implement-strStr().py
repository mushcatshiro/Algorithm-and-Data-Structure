"""
implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string?
This is a great question to ask during an interview.

We will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().


Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0


Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""


class solution_1:

    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    def find_needle(self):
        if len(self.needle) == 0:
            return 0
        if len(self.needle) > len(self.haystack):
            return -1
        for i in range(len(self.haystack) - len(self.needle) + 1):
            # to guarantee the range is always at least 1
            if self.haystack[i: i + len(self.needle)] == self.needle:
                return i
        return -1


class solution_2:

    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    def find_needle(self):
        if self.needle in self.haystack:
            return self.haystack.index(self.needle)
        return -1


assert solution_1('hello', 'll').find_needle() == 2
assert solution_1('aaaaa', 'bba').find_needle() == -1
assert solution_1('aaaaa', 'aaaaa').find_needle() == 0
assert solution_1('', '').find_needle() == 0
assert solution_1('abc', 'c').find_needle() == 2
