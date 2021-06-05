"""
Given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
"""


import add_path
from utilities.data_structures import linked_list_node


def traverse(inp_node: linked_list_node):
    while inp_node:
        print(inp_node.val)
        inp_node = inp_node.next


def build_ll(inp_list: list):
    head = linked_list_node()
    cur = head
    for i in range(len(inp_list)):
        cur.val = inp_list[i]
        if i + 1 == len(inp_list):
            break
        cur.next = linked_list_node()
        cur = cur.next
    return head


class solution_1:
    def __init__(self, LL1_head, LL2_head):
        self.LL1_head = LL1_head
        self.LL2_head = LL2_head

    def add_two_numbers(self):
        L1_cur = self.LL1_head
        L2_cur = self.LL2_head
        ret_head = linked_list_node()
        cur_dummy = ret_head
        carry = 0
        while L1_cur or L2_cur:
            x = L1_cur.val if L1_cur else 0
            y = L2_cur.val if L2_cur else 0
            _sum = carry + x + y
            carry = int(_sum / 10)
            cur_dummy.val = _sum % 10
            L1_cur = L1_cur.next if L1_cur and L1_cur.next else None
            L2_cur = L2_cur.next if L2_cur and L2_cur.next else None
            if L1_cur or L2_cur:
                cur_dummy.next = linked_list_node()
                cur_dummy = cur_dummy.next
            else:
                break
        if carry > 0:
            cur_dummy.next = linked_list_node()
            cur_dummy = cur_dummy.next
            cur_dummy.val = carry
        return ret_head


L1 = build_ll([1, 2, 3, 4, 5])
L2 = build_ll([1, 2, 3, 4, 5])
# L1 = build_ll([0])
# L2 = build_ll([0])
h = solution_1(L1, L2).add_two_numbers()
traverse(h)
