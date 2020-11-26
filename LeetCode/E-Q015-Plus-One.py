"""
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that,
the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


class solution_1:
    def __init__(self, input_array):
        self.input_array = input_array

    def add_one(self):
        for i in range(1, len(self.input_array) + 1):
            temp = self.input_array[-i] + 1
            if temp > 9:
                self.input_array[-i] = 0
            else:
                self.input_array[-i] = temp
                return self.input_array

        return [1] + self.input_array


class solution_2:
    def __init__(self, input_array):
        self.input_array = input_array

    def add_one(self):
        temp = str(int("".join(list(map(str, self.input_array)))) + 1)
        temp = temp.zfill(len(self.input_array))  # question not clear on this
        print(temp)
        temp = list(map(int, temp))
        return temp


assert solution_2([1, 2, 3]).add_one() == [1, 2, 4]
assert solution_2([9]).add_one() == [1, 0]
assert solution_2([0, 0]).add_one() == [0, 1]
