"""
Finds length of longest path from root to leaf
"""

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
	
def get_longest_path(root):
	if not root:
		return 0
	return 1 + max(get_longest_path(root.left), get_longest_path(root.right))
	

if __name__ == "__main__":
	#Empty tree
	assert get_longest_path(None) == 0
	#Single path
	root = Node(10)
	root.left = Node(3)
	assert get_longest_path(root) == 2
	#Multiple paths of same length, case of complete binary tree
	root = Node(10)
	root.left = Node(3)
	root.right = Node(17)
	root.left.left = Node(2)
	root.left.right = Node(4)
	root.right.left = Node(15)
	root.right.right = Node(25)
	assert get_longest_path(root) == 3
	#Variabe length paths
	root.left.left.right = Node(50)
	assert get_longest_path(root) == 4