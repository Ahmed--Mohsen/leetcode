class TrieNode:
	# Initialize your data structure here.
	def __init__(self):
		# reference to related trie node
		self.childern = {}

		# flag to determine if this node represents a word ending
		self.word_end = False

	def add(self, char):
		self.childern[char] = TrieNode()

class Trie:

	def __init__(self):
		self.root = TrieNode()

	# @param {string} word
	# @return {void}
	# Inserts a word into the trie.
	def insert(self, word):
		node = self.root
		for char in word:
			if not char in node.childern:
				node.add(char)
			node = node.childern[char]
		node.word_end = True

	# @param {string} word
	# @return {boolean}
	# Returns if the word is in the trie.
	def search(self, word):
		node = self.root
		for char in word:
			if not char in node.childern:
				return False
			node = node.childern[char]
		return node.word_end
		
	# @param {string} prefix
	# @return {boolean}
	# Returns if there is any word in the trie
	# that starts with the given prefix.
	def startsWith(self, prefix):
		node = self.root
		for char in prefix:
			if not char in node.childern:
				return False
			node = node.childern[char]
		return True
		

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print trie.startsWith("somess")