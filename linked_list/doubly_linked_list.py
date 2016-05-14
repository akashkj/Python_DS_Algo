class DoubleLinkNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None
		
		
class DoublyLinkedList(object):

	def __init__(self):
		self.head = None
		self.current = None

	def create_linked_list(input_list):
		for entry in input_list:
			node = DoubleLinkNode(entry)
			if not self.head:
				self.head = node
				self.current = node
			else:
				node.prev = self.current
				self.current.next = node
				self.current = node
		return self.head