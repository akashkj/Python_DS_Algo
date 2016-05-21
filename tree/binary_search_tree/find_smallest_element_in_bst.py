"""
Find smallest element in a bst
Idea is to recursively navigate to left of tree until the end
"""

def find_smallest_in_bst(root):
	if not root:
		return None
	if not root.left:
		return root.data
	return find_smallest_in_bst(root.left)