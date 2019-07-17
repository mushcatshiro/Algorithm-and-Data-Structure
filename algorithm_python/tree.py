class node(object):
	"""docstring for node"""
	def __init__(self, value):
		# super(node, self).__init__()
		self.value = value
		self.leftNode = None
		self.righNode = None

def insertNode(root, node):
	if (root == None):
		root = node
	else:
		if (root.value > node.value):
			if (root.leftNode == None):
				root.leftNode = node
			else:
				insertNode(root.leftNode, node)
		elif (root.value < node.value):
			if (root.righNode == None):
				root.righNode = node
			else:
				insertNode(root.righNode, node)

def traversal(root):
	if root:
		traversal(root.leftNode)
		print(root.value)
		traversal(root.righNode)

def bin_search(root, value, counter):
	if (root == None):
		print('tree is empty')
	elif (root.value == value):
		print('search is completed after {} search(es)'.format(counter))
	elif (root.value > value):
		print("moving left")
		counter += 1
		bin_search(root.leftNode, value, counter)
	elif (root.value < value):
		print("moving right")
		counter += 1
		bin_search(root.righNode, value, counter)

arr = [18,19,12,7,17,6,8,10,5,3,9,16,2,0,1,4,13,14,15,11]
r = node(arr[0])

for i in range(1, len(arr)):
	insertNode(r, node(arr[i]))

# traversal(r)
bin_search(r, 10, 0)
# python counts the nodes, C counts the links