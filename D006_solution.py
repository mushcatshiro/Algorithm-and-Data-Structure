"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses
"""

# isnt this defeat the purpose to only store a single variable in object?
# XOR of address(B) and npx of C gives us the address(D)
class Node():
    """docstring for Node"""
    def __init__(self, npx=None, val=None):
        self.npx = npx
        self.val = val # for t/s purposes

    def _update_npx(self, npx):
        self.npx = npx

class XORLL(object):
    """docstring for XORLL"""
    def __init__(self, startID=0, endID=0, length=0):
        self.startID = startID
        self.endID = endID # do i need one?
        self.length = length

    # expect lstOfValues is list of strings
    # expect return as boolean
    def _add(self, lstOfValues):
        # add element to end
        self.length += len(lstOfValues)
        linkListNode = []
        for val in lstOfValues:
            linkListNode.append(Node(val=val))

        for index, node in enumerate(linkListNode):
            # check id, updated id to npx
            if index-1 in range(len(linkListNode)) and\
               index+1 in range(len(linkListNode)):
                npx = id(linkListNode[index-1]) ^ id(linkListNode[index+1])
                node._update_npx(npx=npx)
            else:
                npx = id(linkListNode[index])
                node._update_npx(npx=npx)
        return True
        
    def _get(self, index):
        if index > self.length/2:
            print('start with endID')
            node = self._traverse(index, self.endID)
        else:
            print('start with startID')
            node = self._traverse(index, self.startID)
        return node.val

    @staticmethod
    def _traverse(index, id):
        return node
 
def test(n=None, target=None, nodesVal=None):
    # create n nodes
    # find, how?
    assert target < n, 'target > n'
    xorll = XORLL()
    if xorll._add(nodesVal):
        # print(xorll._get(target))
        print('no error')

     
# a = Node()
# b = Node()

# print(id(a)^id(b))
# print(0^id(a))
# print(f'a: {id(a)}, b: {id(b)}')

nodesVal = ['a', 'b', 'c', 'd', 'e']
test(n=len(nodesVal), target=2, nodesVal=nodesVal)