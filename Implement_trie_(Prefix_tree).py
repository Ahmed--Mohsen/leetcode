"""

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""

class TrieNode:ins
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
		
	# return the LCA trie node for the prefix
	def find(self, prefix):
		node = self.root
		for char in prefix:
			if not char in node.childern:
				return node
			node = node.childern[char]
		return node
		
	def all_matches(self, prefix):
		node = self.find(prefix)
		result = []
		self.all_matches_helper(node, prefix, result)
		return result
		
	def all_matches_helper(self, root, prefix, result):
		# base case nothing to be done
		if root == None:
			return
			
		# the current prefix is actually a valid word
		if root.word_end:
			result.append(prefix)
		
		# DFS search for other children
		for char in root.childern:
			self.all_matches_helper(root.childern[char], prefix + char, result)
			

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
trie.insert("sometimes")
trie.insert("something")

#print trie.startsWith("somess")
#print trie.find("some").childern
print trie.all_matches("some")