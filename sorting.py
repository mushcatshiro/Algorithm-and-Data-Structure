"""
python assignment is a pointer/reference
thus all changes are in place (to the root input_list)
"""

# worst case O(n^2), on average O(nlogn)
# how to prevent worst case? choose pivot carefully, median of three
class QuickSort():
    """docstring for QuickSort"""
    def __init__(self, input_list, left=None, right=None):
        self.input_list = input_list
        self.left = left
        self.right = right

    def _sort(self):
        i = self.left - 1
        pivot = self.input_list[self.right]
        print(f'in _sort, i: {i}, pivot: {pivot},\
              left: {self.left}, right: {self.right}')

        # fix last item in array as pivot
        # from left and from right, ensure we swap into left < pivot < right
        # then left + 1 swap with pivot
        # return pivot index such that subsequent call is 0: PI or PI: end
        for j in range(self.left, self.right):
            if self.input_list[j] <= pivot:
                print(f'inp_j {self.input_list[j]},\
                      pivot {pivot}, i {i+1}, j {j}')
                i += 1
                self.input_list[i], self.input_list[j] =\
                    self.input_list[j], self.input_list[i]
                print(self.input_list)
        self.input_list[i+1], self.input_list[self.right] =\
            self.input_list[self.right], self.input_list[i+1]
        print(f'end _sort {self.input_list}')
        return (i+1)

    def get_sorted_list(self):
        print('start ', self.input_list)
        if self.left is None:
            self.left = 0
        if self.right is None:
            self.right = len(self.input_list) - 1

        if self.left < self.right:
            partitionIndex = self._sort()
            print(f'partitionIndex {partitionIndex}')

            l = QuickSort(self.input_list, self.left, partitionIndex-1)
            l.get_sorted_list()
            r = QuickSort(self.input_list, partitionIndex+1, self.right)
            r.get_sorted_list()

        print('end ', self.input_list)
        return self.input_list


# O(n^2)
class BubbleSort():
    """docstring for BubbleSort"""
    def __init__(self, input_list):
        self.input_list = input_list

    # double for loop, 2nd for loop -1 
    # because on first attempt the largest item will be pushed to right end
    def get_sorted_list(self):

        for j in range(len(self.input_list)):
            for i in range(len(self.input_list) - 1):
                if self.input_list[i+1] < self.input_list[i]:
                    self.input_list[i+1], self.input_list[i] =\
                        self.input_list[i], self.input_list[i+1]
        return self.input_list


# O(nlogn)
# to revise on recursion
class MergeSort():
    """docstring for MergeSort"""
    def __init__(self, input_list):
        self.input_list = input_list

    def get_sorted_list(self):

        if len(self.input_list) > 1:
            mid = len(self.input_list) // 2
            left = self.input_list[:mid]
            right = self.input_list[mid:]

            leftsort = MergeSort(left)
            leftsort.get_sorted_list()
            rightsort = MergeSort(right)
            rightsort.get_sorted_list()

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.input_list[k] = left[i]
                    i += 1
                else:
                    self.input_list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.input_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.input_list[k] = right[j]
                j += 1
                k += 1

        return self.input_list
    

def test_sort_algo():
    input_list_odd = [9, 5, 6, 3, 7, 1, 2]
    input_list_even = [9, 5, 6, 3, 7, 1, 2, 8]

    q1 = QuickSort(input_list=input_list_odd)
    q2 = QuickSort(input_list=input_list_even)

    assert q1.get_sorted_list() == [1, 2, 3, 5, 6, 7, 9], 'q1 doesnt match'
    # assert q2.get_sorted_list() == [1, 2, 3, 5, 6, 7, 8, 9], 'q2 doesnt match'


test_sort_algo()
