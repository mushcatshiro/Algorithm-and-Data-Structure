class node:
    def __init__(self, value=0):
        self.value = value


class linked_list_node(node):
    def __init__(self, value=0, next=None):
        super().__init__(value=value)
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def traverse_to_list(self):
        return_list = []
        temp = self.head
        while temp:
            return_list.append(temp.value)
            temp = temp.next
        return return_list

    def add_node(self, value):
        new_node = linked_list_node(value)
        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = new_node


class tree_node(node):
    def __init__(self, value=None, left=None, right=None):
        super().__init__(value=value)
        self.left = left
        self.right = right


class tree:
    """
    constrains #1 : no duplicated numbers
    """
    def __init__(self, root=None):
        self.root = root

    def insert_tree_node(self, value):
        self._insert_tree_node(self.root, value)

    def _insert_tree_node(self, root, value):
        if root is None:
            self.root = tree_node(value=value)
        else:
            if (root.value < value):
                if root.right is None:
                    root.right = tree_node(value=value)
                else:
                    self._insert_tree_node(root.right, value)
            elif (root.value > value):
                if root.left is None:
                    root.left = tree_node(value=value)
                else:
                    self._insert_tree_node(root.left, value)
            else:
                print(f"duplicated value {value} will not be added to tree")

    def traversal(self, node=None):
        if node:

            self.traversal(node.left)
            print(node.value)
            self.traversal(node.right)


# bst