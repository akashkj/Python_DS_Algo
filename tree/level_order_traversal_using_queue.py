class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
def level_order_traversal(tree):
	if not tree:
		return
	queue = [tree]
	while queue:
		node_to_process = queue[0]
		print node_to_process.data
		del queue[0]
		if node_to_process.left:
			queue.append(node_to_process.left)
		if node_to_process.right:
			queue.append(node_to_process.right)
	
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left =  Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	level_order_traversal(root)