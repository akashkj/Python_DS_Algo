class TrieNode(object):

	def __init__():
		self.next = {}
		self.complete_word = False
		
	def add_word(word):
		if not word:
			self.complete_word = True
			return
		node_key = word[0]
		remaining_word = word[1:]
		if node_key in self.next:
			self.next.get(node_key).add_word(remaining_word)
		else:
			trie_node = TrieNode()
			self.next[node_key] = trie_node
			trie_node.add_word(remaining_word)