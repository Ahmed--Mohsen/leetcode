"""

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

"""

class TrieNode:
	# Initialize your data structure here.
	def __init__(self):
		# reference to related trie node
		self.children = {}

		# flag to determine if this node represents a word ending
		self.word_end = False

	def add(self, char):
		self.children[char] = TrieNode()

class Trie:

	def __init__(self):
		self.root = TrieNode()

	# @param {string} word
	# @return {void}
	# Inserts a word into the trie.
	def insert(self, word):
		node = self.root
		for char in word:
			if not char in node.children:
				node.add(char)
			node = node.children[char]
		node.word_end = True
		
class Solution:
	
	# @param {character[][]} board
	# @param {string[]} words
	# @return {string[]}
	def findWords(self, board, words):
		
		# base case
		if len(words) == 0 or len(board) == 0:
			return []
			
		self.board = board
		
		# create a trie for fast prefix lookup
		self.trie = Trie()
		for word in words:
			self.trie.insert(word)
		
		# visited flag for each char in board 
		self.visited = [[False] * len(board[0]) for i in range(len(board))]
		
		# result set
		self.result = []

		# DFS search from all possible chars
		for i in range(len(board)):
			for j in range(len(board[0])):
				self.traverse(i, j, "", self.trie.root)
		return self.result
	
	def traverse(self, row, colm, current, root):
		
		# already visited before
		if self.visited[row][colm]: 
			return
		
		# word currently searched is not present
		current_char = self.board[row][colm]
		if not current_char in root.children:
			return
		
		# update current word
		current += self.board[row][colm]
		next_root = root.children[current_char]
		
		# found a valid word
		if next_root.word_end:
			self.result.append(current)
			next_root.word_end = False # prevent duplications
			
		# mark current word as visited
		self.visited[row][colm] = True
			
		# move up
		if row > 0:
			self.traverse(row - 1, colm, current, next_root)
	
		# move down
		if row < len(self.board) - 1:
			self.traverse(row + 1, colm, current, next_root)
	
		# movel left
		if colm > 0:
			self.traverse(row, colm - 1, current, next_root)
	
		# move right
		if colm < len(self.board[0]) - 1:
			self.traverse(row, colm + 1, current, next_root)
	
		# backtrack
		self.visited[row][colm] = False
			
		
s = Solution()
print s.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"])
