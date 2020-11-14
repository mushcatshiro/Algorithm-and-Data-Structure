"""
Given an array nums and a value val, 
remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. 
It doesn't matter what you leave beyond the new length.
"""


class solution_1:
    def __init__(self, input_list, val):
        self.input_list = input_list
        self.val = val

    def remove_element(self):
        i = 0
        while i < len(self.input_list):
            if self.input_list[i] == self.val:
                self.input_list.pop(i)
            else:
                i += 1
        return len(self.input_list)


assert solution_1([1, 2, 3, 4, 5, 5], 5).remove_element() == 4
