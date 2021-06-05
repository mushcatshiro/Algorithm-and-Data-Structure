"""
The count-and-say sequence is a sequence of digit strings
defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.
To determine how you "say" a digit string,
split it into the minimal number of groups
so that each group is a contiguous section all of the same character.
Then for each group,
say the number of characters,
then say the character.
To convert the saying into a digit string,
replace the counts with a number and concatenate every saying.
"""


class solution_1:
    def __init__(self, n):
        self.n = n

    def count_and_say(self):
        temp = '1'

        for i in range(self.n - 1):
            print(f'temp: {temp}')
            newtemp = ''
            j = 0
            while j < len(temp):
                count = 1
                while j < len(temp) - 1 and temp[j] == temp[j + 1]:
                    count += 1
                    j += 1
                print(count, temp[j])
                newtemp += str(count) + temp[j]
                j += 1
            temp = newtemp
        return temp


assert solution_1(3).count_and_say() == '21'
assert solution_1(4).count_and_say() == '1211'