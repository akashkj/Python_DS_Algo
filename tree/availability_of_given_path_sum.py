"""
Path sum is sum of node values from root to leaf nodes
Check if the input sum is present in the tree
"""


class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None	

		
def is_path_sum_present(root, sum):
	if not root:
		return False
	current_sum = sum - root.data
	if not root.left and not root.right:
		if current_sum == 0:
			return True
		return False
	return is_path_sum_present(root.left, current_sum) or is_path_sum_present(root.right, current_sum)
	

if __name__ == "__main__":
	#Empty tree
	assert is_path_sum_present(None, 10) == False
	#Single path
	root = Node(10)
	root.left = Node(3)
	assert is_path_sum_present(root, 13) == True
	assert is_path_sum_present(root, 10) == False
	#Multiple paths of same length, case of complete binary tree
	root.right = Node(17)
	root.left.left = Node(2)
	root.left.right = Node(4)
	root.right.left = Node(15)
	root.right.right = Node(25)
	assert is_path_sum_present(root, 10) == False
	assert is_path_sum_present(root, 15) == True
	#Variabe length paths
	root.left.left.right = Node(50)
	#assert get_longest_path(root) == 4