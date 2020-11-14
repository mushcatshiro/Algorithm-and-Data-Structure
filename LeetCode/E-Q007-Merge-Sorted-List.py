"""
Merge two sorted linked lists and return it as a new sorted list.
The new list is made by splicing together the nodes of the first two lists.
"""

import sys
from config import SYSPATH_DIR
sys.path.append(SYSPATH_DIR)
from utilities.data_structures import linked_list, linked_list_node


class solution_1:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def merge(self):
        merged_list = linked_list_node()
        temp = merged_list

        while True:
            if self.l1 is None:
                temp.next = self.l2
                break
            if self.l2 is None:
                temp.next = self.l1
                break

            if self.l1.value <= self.l2.value:
                temp.next = self.l1
                self.l1 = self.l1.next
            else:
                temp.next = self.l2
                self.l2 = self.l2.next

            temp = temp.next
        return merged_list.next


def prep_linked_list(input_list):
    ll = linked_list()
    for value in input_list:
        ll.add_node(value)
    return ll


l1 = prep_linked_list([1, 2, 3, 4])
l2 = prep_linked_list([5, 6, 7, 8])

m_list = solution_1(l1=l1.head, l2=l2.head).merge()
while m_list.value:
    print(m_list.value)
    m_list = m_list.next
    if m_list is None:
        break
