class LinkNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None


class LinkedList(object):

	def __init__(self):
		self.head = None
		self.current = None
		
	def create_linked_list_from_list(self, input_list):
		for entry in input_list:
			node = LinkNode(entry)
			if not self.head:
				self.head = node
				self.current = node
			self.current.next = node
			self.current = node
		return self.head