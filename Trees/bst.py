class node:
	left_child = None
	right_child = None
	data = none
	def __init__(self, data, lc, rc):
		self.data = data
		self.left_child = lc
		self.right_child = rc


class bst:
	root = None

	def __init__(self, root=None):
		self.root = root

	def insert(data):
		current_node = root

		if current_node is None: 
			root = node(data, None, None)
			return root

		while(current_node!=None):
			if data>=current_node.data: 
				if(not current_node.right_child):
					current_node.right_child = node(data, None, None)
					current_node = None
				else:
					current_node = current_node.right_child
			else:
				if(not current_node.left_child):
					current_node.left_child = node(data, None, None)
					current_node = None
				else:
					current_node = current_node.left_child
	




