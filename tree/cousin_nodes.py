"""
Find if two nodes of a tree are cousins i.e. same level but different parents
Solution: Level order traversal and keep track of wheter nodes found and their parents are not same
"""
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.level = None
		
def are_nodes_cousin(root, node1, node2):
	if not any([root, node1, node2]):
		return False
	nodes_to_check = [node1, node2]
	node1_found = False
	node2_found = False
	root.level = 1
	q = [root]
	while q:
		current = q[0]
		left = current.left
		right = current.right
		if left in nodes_to_check and right in nodes_to_check:
			return False
		if left:
			left.level = current.level + 1
			q.append(left)
		if right:
			right.level = current.level + 1
			q.append(right)
		del q[0]
		node1_found = node1_found or node1 == left or node1 == right
		node2_found = node2_found or node2 == left or node2 == right
		if node1_found and node2_found and node1.level == node2.level:
			return True
	return False
		

if __name__ == "__main__":
	#Empty tree
	assert are_nodes_cousin(None, None, None) == False
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.right.right = Node(15)
	root.right.left = Node(6)
	root.right.right = Node(7)
	root.right.left.right = Node(8) 
	#Cousin nodes
	node1 = root.left.right
	node2 = root.right.right
	assert are_nodes_cousin(root, node1, node2) == True
	#Sibling nodes
	node1 = root.left
	node2 = root.right
	assert are_nodes_cousin(root, node1, node2) == False
	#Non cousins
	node1 = root.left.left
	node2 = root.right
	assert are_nodes_cousin(root, node1, node2) == False