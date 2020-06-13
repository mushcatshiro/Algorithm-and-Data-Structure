class Node():
    """docstring for Node"""
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class BinaryTree():
    """docstring for BinaryTree"""
    def __init__(self, Tree=None, ValueList=None):
        self.ValueList = ValueList
        self.Tree = self.BuildTree()

    def BuildTree(self):
        assert type(self.ValueList) == list, 'please provide in list format'

        for i in self.ValueList:
            pass


b = BinaryTree(ValueList=[1, 2])
        