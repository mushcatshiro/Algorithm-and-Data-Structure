"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same
if they are structurally identical and the nodes have the same value.

eg.1
   1         1
  / \       / \
 2   3     2   3
true

eg.2
  1         1
 /           \
2             2
false

eg.3
  1         1
 / \       / \
2   1     1   2
false
"""

import add_path
from utilities.data_structures import tree


l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4, 5, 6, 8]


def build_tree(list_of_number):
    t = tree()
    for i in list_of_number:
        t.insert_tree_node(i)
    return t.root


r1, r2, r3 = build_tree(l1), build_tree(l1), build_tree(l2)


class solution:

    def tree_matching(self, node_one, node_two):
        if node_one is None and node_two is None:
            return True
        if node_one is None or node_two is None:
            return False
        if node_one.value != node_two.value:
            return False
        return self.tree_matching(node_one.left, node_two.left) and\
            self.tree_matching(node_one.right, node_two.right)


assert solution().tree_matching(r1, r2) == True
assert solution().tree_matching(r1, r3) == False