"""

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true 

"""
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
		return self.search_helper(self.root, word, 0)
		
	def search_helper(self, root, word, index):
		# base case
		if index == len(word):
			return root.word_end
		
		char = word[index]

		# wild matching case
		if char == ".":
			for c in root.childern:
				if self.search_helper(root.childern[c], word, index + 1):
					return True
		
		# normal matching	case
		else:
			if char in root.childern:
				return self.search_helper(root.childern[char], word, index + 1) 
		
		# match failed		
		return False
			

		
class WordDictionary:
	
	def __init__(self):
		self.dict = Trie()

	# @param {string} word
	# @return {void}
	# Adds a word into the data structure.
	def addWord(self, word):
		self.dict.insert(word)

	# @param {string} word
	# @return {boolean}
	# Returns if the word is in the data structure. A word could
	# contain the dot character '.' to represent any one letter.
	def search(self, word):
		return self.dict.search(word)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("..r.")
