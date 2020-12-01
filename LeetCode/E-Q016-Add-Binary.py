"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""


class solution_1:
    def __init__(self, input_one, input_two):
        self.input_one = input_one
        self.input_two = input_two

    def add_binary(self):
        temp = bin(int(self.input_one, 2) + int(self.input_two, 2))
        return temp[2:]


class solution_2:
    def __init__(self, input_one, input_two):
        self.input_one = input_one
        self.input_two = input_two

    def add_binary(self, a=None, b=None):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.add_binary(self.add_binary(a[0: -1], b[0: -1]), '1') +\
                '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.add_binary(a[0: -1], b[0: -1]) + '0'
        else:
            return self.add_binary(a[0: -1], b[0: -1]) + '1'


class solution_3:
    def __init__(self, input_one, input_two):
        self.input_one = input_one
        self.input_two = input_two

    def add_binary(self, a, b):
        sums = {
            '000': '0',
            '001': '1',
            '010': '1',
            '100': '1',
            '011': '10',
            '110': '10',
            '101': '10',
            '111': '11',
        }
        carry_over = '0'

        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))

        answer = []
        for i in range(len(a) - 1, -1, -1):
            answer.append(sums[a[i] + b[i] + carry_over][-1])
            if len(sums[a[i] + b[i] + carry_over]) > 1:
                carry_over = '1'
            else:
                carry_over = '0'
        if carry_over == '1':
            answer.append(carry_over)
        return ''.join(reversed(answer))

assert solution_1("11", "1").add_binary() == "100"
assert solution_1("1010", "1011").add_binary() == "10101"

t1 = solution_3("11", "1")
t2 = solution_3("1010", "1011")
assert t1.add_binary(t1.input_one, t1.input_two) == "100"
assert t2.add_binary(t2.input_one, t2.input_two) == "10101"
