"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?
"""


class solution_1:
    def __init__(self, input_integer):
        self.input_integer = input_integer
        self.length = len(str(input_integer))
        self.is_even = True if len(str(input_integer)) % 2 == 0 else False

    def is_palindrome(self):
        if self.input_integer < 0:
            return False
        if self.is_even:
            return str(self.input_integer)[:int(self.length / 2)] \
                == str(self.input_integer)[int(self.length / 2):][::-1]
        else:
            return str(self.input_integer)[:int(self.length / 2)] \
                == str(self.input_integer)[int(self.length / 2) + 1:][::-1]


class solution_2:
    def __init__(self, input_integer):
        self.input_integer = input_integer
        self.length = len(str(input_integer))
        self.is_even = True if len(str(input_integer)) % 2 == 0 else False

    def is_palindrome(self):
        reverted_num = 0
        while (self.input_integer > reverted_num):
            reverted_num = reverted_num * 10 + self.input_integer % 10
            self.input_integer = int(self.input_integer / 10)
        return self.input_integer == reverted_num \
            or self.input_integer == int(reverted_num / 10)


assert solution_2(123321).is_palindrome() == True
assert solution_2(123322).is_palindrome() == False
assert solution_2(1234321).is_palindrome() == True
assert solution_2(1234322).is_palindrome() == False
assert solution_2(10).is_palindrome() == False