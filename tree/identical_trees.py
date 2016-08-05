"""
Checks if two trees are identical. Trees are said to be indetical if they have exactly same structure.
Solution: Traverse recursively and check for equality of data of both trees at the same time
"""

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
def are_trees_identical(root1, root2):
	"""
	:param root1: root of first tree
	:param root2: root of second tree
	"""
	if not root1 and not root2:
		return True
	if root1 and root2:
		return root1.data == root2.data and are_trees_identical(root1.left, root2.left) and are_trees_identical(root1.right, root2.right)
	return False #either one of the node is None, so not identical
	
if __name__ == "__main__":
	#Empty trees
	assert are_trees_identical(None, None) == True
	#Non-identical trees with same number of nodes
	root1 = Node(5)
	root1.left = Node(3)
	root1.right = Node(10)
	root2 = Node(5)
	root2.left = Node(3)
	root2.right = Node(15)
	assert are_trees_identical(root1, root2) == False
	#Non-identical trees with different number of nodes
	root1 = Node(5)
	root1.left = Node(3)
	root1.right = Node(10)
	root2 = Node(5)
	root2.left = Node(3)
	root2.right = Node(10)
	root2.right.left = Node(20)
	assert are_trees_identical(root1, root2) == False
	#Identical trees
	root1 = Node(5)
	root1.left = Node(3)
	root1.right = Node(10)
	root2 = Node(5)
	root2.left = Node(3)
	root2.right = Node(10)
	assert are_trees_identical(root1, root2) == True