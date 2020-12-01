"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""
import add_path
from utilities.data_structures import linked_list


def prep_linked_list(input_list):
    ll = linked_list()
    for value in input_list:
        ll.add_node(value)
    return ll


def traverse(linked_list_head):
    ret_list = []
    current = linked_list_head
    while current:
        ret_list.append(current.value)
        current = current.next
    return ret_list


class solution_1:
    def __init__(self, linked_list_head):
        self.linked_list_head = linked_list_head

    def remove_duplicate(self):
        current = self.linked_list_head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return self.linked_list_head


l1 = prep_linked_list([1, 1, 2, 3, 3, 4])

assert traverse(solution_1(l1.head).remove_duplicate()) == [1, 2, 3, 4]
