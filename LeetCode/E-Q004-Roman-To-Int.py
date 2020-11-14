"""
Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.
"""

"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
IV            4
IX            9
XL            40
XC            90
CD            400
CM            900

Constraints
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

class solution_1:
    def __init__(self, input_roman_string):
        self.input_roman_string = input_roman_string
        self.checklist = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_integer(self):
        ret = 0
        for i in range(len(self.input_roman_string) - 1):
            if self.checklist[self.input_roman_string[i]] <\
               self.checklist[self.input_roman_string[i + 1]]:
                ret = ret - self.checklist[self.input_roman_string[i]]
            else:
                ret = ret + self.checklist[self.input_roman_string[i]]
        ret += self.checklist[self.input_roman_string[-1]]
        return ret

assert solution_1('IX').roman_to_integer() == 9
assert solution_1('XL').roman_to_integer() == 40
assert solution_1('MCMIV').roman_to_integer() == 1904

# there exists a solution with while loop that requires nested if