"""
Given head, the head of a linked list,
determine if the linked list has a cycle in it.

There is a cycle in a linked list
if there is some node in the list that can be reached again
by continuously following the next pointer.
Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

e1
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list
where the tail connects to the 1st node (0-indexed).

e2
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list,
where the tail connects to the 0th node.

e3
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

tag: two pointers
"""


def hasCycle(self, head) -> bool:
    if not head:
        return False
    i = head
    j = head.next
    while i is not None and j is not None and j.next is not None:
        if j == i:
            return True
        i = i.next
        j = j.next.next
    return False


"""
take note j.next.next instead of j.next
this is due to ensure that if there is a cycle,
two pointers **will** eventually meet. (j.next will never)
"""