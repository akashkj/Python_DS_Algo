"""
Checks if a tree is symmetric i.e. mirror of itself
     1
   /   \
  2     2
 / \   / \
3   4 4   3
is symmetric as when we create the mirror, same tree is obtained.
Solution: Use same tree to compare recursively such that root value of both are equal and left child of first equal to right child of second and vice versa
"""

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
def _symmetric_check_helper(root1, root2):
	if not root1 and not root2:
		return True
	if root1 and root2:
		return root1.data == root2.data and _symmetric_check_helper(root1.left, root2.right) and _symmetric_check_helper(root1.right, root2.left)
	return False
	
	
def is_tree_symmetric(root):
	if not root:
		return True
	return _symmetric_check_helper(root, root)
	
if __name__ == "__main__":
	#Empty tree
	assert is_tree_symmetric(None) == True
	#Not a symmetric tree
	#         1
    #       /   \
    #      2     3
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	assert is_tree_symmetric(root) == False
	#Symmetric tree
	#         1
    #       /   \
    #      2     2
    #     / \   / \
	#    3   4 4   3
	root = Node(1)
	root.left = Node(2)
	root.left.left = Node(3)
	root.left.right = Node(4)
	root.right = Node(2)
	root.right.left = Node(4)
	root.right.right = Node(3)
	assert is_tree_symmetric(root) == True