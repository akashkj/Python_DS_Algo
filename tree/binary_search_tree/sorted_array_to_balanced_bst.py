"""
Problem: Convert a sorted array to balanced binary search tree
Solution: Find mid of array as root and recursively find left and right child as middle of sub-trees
"""

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
def _convert_array_to_balanced_bst(arr, start, end):
	"""
	:param arr: list of numbers in sorted order
	:param start: integer start index of arr
	:param end: integer end index of arr
	:return: Node object defining root of tree
	"""
	if start > end:
		return None
	mid = (start + end) / 2
	node = Node(arr[mid])
	node.left = _convert_array_to_balanced_bst(arr, start, mid - 1)
	node.right = _convert_array_to_balanced_bst(arr, mid + 1, end)
	return node
	
def inorder_traversal(root):
	"""
	:param root: Node object defining root of tree
	"""
	if not root:
		return
	inorder_traversal(root.left)
	print root.data,
	inorder_traversal(root.right)
	
def convert_array_to_bst(arr):
	"""
	:param arr: list of numbers in sorted order
	:return: Node object defining root of tree
	"""
	input_size = len(arr)
	if input_size == 0:
		return None
	return _convert_array_to_balanced_bst(arr, 0, input_size - 1)
	
if __name__ == "__main__":
	root = convert_array_to_bst([1, 2, 3])
	inorder_traversal(root)
	print ""
	root = convert_array_to_bst([1, 2, 3, 4])
	inorder_traversal(root)
	

	
