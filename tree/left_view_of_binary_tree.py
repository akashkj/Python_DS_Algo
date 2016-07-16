class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
def level_order_traversal(tree):
	height = get_tree_height(tree)
	for i in range(1, height + 1):
		traverse_a_level(tree, i)
	
def traverse_a_level(tree, level_to_traverse):
	if not tree:
		return
	if level_to_traverse == 1:
		print tree.data,
	elif level_to_traverse > 1:
		traverse_a_level(tree.left, level_to_traverse - 1) if tree.left else traverse_a_level(tree.right, level_to_traverse - 1)

def get_tree_height(tree):
	if not tree:
		return 0
	return 1 + max(get_tree_height(tree.left), get_tree_height(tree.right))
	
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left =  Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	level_order_traversal(root)