"""
Given a sorted array nums, 
remove the duplicates in-place such that each element appears only once 
and returns the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
"""


class solution_1:
    def __init__(self, input_array):
        self.input_array = input_array

    def remove_duplicates(self):
        i = 0
        j = 1
        while i < len(self.input_array):
            if j == len(self.input_array):
                break
            if self.input_array[i] == self.input_array[j]:
                self.input_array.pop(j)
            elif self.input_array[i] < self.input_array[j]:
                i += 1
                j += 1
        print(self.input_array)
        return len(self.input_array)


assert solution_1([1, 2, 4, 4, 4, 5]).remove_duplicates() == 4
