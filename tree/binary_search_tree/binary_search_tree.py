"""
Binary search tree python implementation
"""

class BinaryNode(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		

class BST(object):

	def __init__(self):
		self.root = None
		
	def add(self, data):
		node = BinaryNode(data)
		if not self.root:
			self.root = node
		else:
			self._add(node, self.root)
		return self.root
					
	def _add(self, node, parent):
		parent_data = parent.data
		node_data = node.data
		if node_data <= parent_data:
			if not parent.left:
				parent.left = node
			else:
				self._add(node, parent.left)
		elif node_data > parent_data:
			if not parent.right:
				parent.right = node
			else:
				self._add(node, parent.right)
				
	def print_inorder(self, root):
		if not root:
			return
		self.print_inorder(root.left)
		print root.data
		self.print_inorder(root.right)
		
	def search(self, data):
		if not data or not self.root:
			return "Not found"
		return self._search(data, root)
	
	def _search(self, data, root):
		if root.data == data:
			return "Found"
		elif data < root.data:
			return self._search(data, root.left)
		elif data > root.data:
			return self._search(data, root.right)

			
if __name__ == "__main__":
	bst = BST()
	root = bst.add(10)
	bst.add(3)
	bst.add(5)
	bst.add(15)
	bst.add(15)
	bst.add(10)
	print bst.print_inorder(root)
	print "search 5 ", bst.search(5)
	print "search 0 ", bst.search(0)
	print "search None ", bst.search(None)
		