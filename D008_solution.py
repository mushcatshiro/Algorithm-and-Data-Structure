"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""
def traverse(node):
    if node.val is not None:
        print(node.val)
    if node.left:
        traverse(node.left)
    if node.right:
        traverse(node.right)

class Node():
    """docstring for Node"""
    def __init__(self, val=None, val2=None, left=None, right=None):
        self.val = val
        self.val2 = val2 # t/s learning purpose
        self.left = left
        self.right = right

    # def traverse(self, direction=None):
    #     print(self.val)
    #     if self.left:
    #         self.traverse(self.left)
    #     if self.right:
    #         self.traverse(self.right)'
    # no idea how to fix yet

root = Node(val=0, val2=14)
root.left = Node(val=1)
root.right = Node(val=0, val2=13)
root.right.left = Node(val=1)
root.right.right = Node(val=0, val2=15)
root.right.left.left = Node(val=1)
root.right.left.right = Node(val=1)

class Solution_1():
    """docstring for solution1"""
    # def __init__(self, rootNode=None):
    #     self.rootNode = rootNode
    #     self.count = 0

    def Count_UniVal(self, rootNode):
        is_uni, count = self.Is_UniVal(root, 0)
        return count

    def Is_UniVal(self, root, count):
        if not root:
            return True, count
        left, count = self.Is_UniVal(root.left, count)
        right, count = self.Is_UniVal(root.right, count)

        if self.is_same(root, root.left, left) and\
            self.is_same(root, root.right, right):
            print(root.val, root.val2)
            count += 1
            return True, count
        # if node.left == None and node.right == None:
        #     return True
        # if node.left != None and node.left.val != node.val:
        #     return False
        # if node.right != None and node.right.val != node.val:
        #     return False
        print(f'returning false at {root.val}, {root.val2}')
        return False, count

    def is_same(self, root, child, is_uni):
        return not child or (is_uni and root.val == child.val)

s = Solution_1()
print(s.Count_UniVal(root))