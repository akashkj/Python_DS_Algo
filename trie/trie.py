class Node:
	
	def __init__(self, value=None):
		self.value = value
		self.children = []
		self.word_end = False


class Trie:

	def __init__(self):
		self.root = Node()
		
	def insert(self, word):
		pass
		
	def search(self, word):
		pass
		
	def delete(self, word):
		pass