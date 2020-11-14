"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""

constrains
list length between 0 to 200 incl
str length between 0 to 200 incl
only lower-case
"""


class solution_1:
    def __init__(self, input_list):
        self.input_list = input_list

    def lcp(self):
        if len(self.input_list) == 0:
            return ''
        for i in range(len(self.input_list[0])):
            c = self.input_list[0][i]
            for j in range(1, len(self.input_list)):
                if i == len(self.input_list[j]) or self.input_list[j][i] != c:
                    return self.input_list[0][0:i]
        return self.input_list[0]


assert solution_1(["flower", "flow", "flight"]).lcp() == 'fl'
assert solution_1(["dog", "racecar", "car"]).lcp() == ''
