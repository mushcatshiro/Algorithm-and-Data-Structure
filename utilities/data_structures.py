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
    def __init__(self, arg):
        self.arg = arg

# bst