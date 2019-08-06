class node:
	"""docstring for node"""
	def __init__(self, value):
		# super(node, self).__init__()
		self.value = value
		self.leftNode = None
		self.righNode = None

class tree:

	def __init__(self, root = None):
		self.root = root

	def insertNode(self, node):
		self._insertNode(self.root, node)


	def _insertNode(self, root, node):
		if (root == None):
			self.root = node
			return (self.root)
		else:
			if (root.value > node.value):
				if (root.leftNode == None):
					root.leftNode = node
				else:
					self._insertNode(root.leftNode, node)
			elif (root.value < node.value):
				if (root.righNode == None):
					root.righNode = node
				else:
					self._insertNode(root.righNode, node)

	def traversal(self, node):
		if node:
			self.traversal(node.leftNode)
			print(node.value)
			self.traversal(node.righNode)

	def bin_search(self, value, counter):
		if (self.root == None):
			print('tree is empty')
		elif (self.root.value == value):
			print('search is completed after {} search(es)'.format(counter))
		elif (self.root.value > value):
			print("moving left")
			counter += 1
			self.bin_search(self.root.leftNode, value, counter)
		elif (self.root.value < value):
			print("moving right")
			counter += 1
			self.bin_search(self.root.righNode, value, counter)

if __name__ == '__main__':
	arr = [18,19,12,7,17,6,8,10,5,3,9,16,2,0,1,4,13,14,15,11]
	r = node(arr[0])
	tree1 = tree(r)

	for i in range(1, len(arr)):
		tree1.insertNode(node(arr[i]))

	tree1.traversal(r)
	# tree1.bin_search(10, 0)
