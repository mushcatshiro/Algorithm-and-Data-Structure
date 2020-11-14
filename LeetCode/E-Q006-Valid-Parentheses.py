"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class solution_1:
    def __init__(self, input_brackets):
        self.input_brackets = input_brackets
        self.match = {'(': ')', '[': ']', '{': '}'}
        self.stack = []

    def validate(self):
        for i in range(len(self.input_brackets)):
            if self.input_brackets[i] not in list(self.match.values()):
                self.stack.append(self.input_brackets[i])
                continue
            if self.input_brackets[i] == self.match[self.stack[-1]]:
                self.stack.pop(-1)
        return True if len(self.stack) == 0 else False


assert solution_1('{}{}{}{}{}{}').validate() is True
assert solution_1('{)').validate() is False
assert solution_1('([{}])').validate() is True
assert solution_1('(([{}]){}]').validate() is False
assert solution_1('(([{}]){})').validate() is True
