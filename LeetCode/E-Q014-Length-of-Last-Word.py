"""
Given a string s consists of some words separated by spaces,
return the length of the last word in the string.
If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '
"""


# python way
class solution_1:
    def __init__(self, input_string):
        self.input_string = input_string

    def length_of_last_word(self):
        if self.input_string == " ":
            return 0
        splited_word_list = self.input_string.strip().split(" ")
        last_word = splited_word_list[-1]
        return len(last_word)


class solution_2:
    def __init__(self, input_string):
        self.input_string = input_string

    def length_of_last_word(self):
        string_length = len(self.input_string) - 1
        last_word_length = 0

        while string_length >= 0 and self.input_string[string_length] == " ":
            print('1st')
            string_length -= 1

        while string_length >= 0 and self.input_string[string_length] != " ":
            last_word_length += 1
            string_length -= 1
            print('2nd')
        print('end')
        return last_word_length


assert solution_2("a ").length_of_last_word() == 1
assert solution_2(" a ").length_of_last_word() == 1
assert solution_2("a asdf").length_of_last_word() == 4
assert solution_2("a asdf ").length_of_last_word() == 4