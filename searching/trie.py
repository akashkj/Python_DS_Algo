class TrieNode(object):

	def __init__():
		self.next = {}
		self.complete_word = False
		
	def add_word(word):
		if is_integer(word):
			return
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
			
	def search_word(word):
		if len(word) == 0:
			print "%s found in the records" % word
			return
		key = word[0]
		remaining_word = word[1:]
		if key in self.next:
			node = self.next.get(key)
			if len(remaining_word) == 0:
				if node.complete_word:
					print "word found in the records"
				else:
					print "word not found in the records"
				return
			node.search(remaining_word)
		print "word not found in the records"