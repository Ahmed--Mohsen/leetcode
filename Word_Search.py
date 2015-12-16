"""

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""

class Solution:
	
	# @param board, a list of lists of 1 length string
	# @param word, a string
	# @return a boolean
	def exist(self, board, word):
		if len(word) == 0 or len(board) == 0:
			return False
		self.board = board
		self.word = word
		self.visited = [[False] * len(board[0]) for i in range(len(board))]

		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.traverse(i, j, 0):
					return True
		return False
	
	def traverse(self, row, colm, word_index):
		if word_index == len(self.word):
			return True
			
		if self.in_board(row, colm):
			if self.visited[row][colm] == False and self.board[row][colm] == self.word[word_index]:
				self.visited[row][colm] = True
				
				if self.traverse(row - 1, colm, word_index + 1):
					return True
				if self.traverse(row + 1, colm, word_index + 1):
					return True
				if self.traverse(row, colm - 1, word_index + 1):
					return True
				if self.traverse(row, colm + 1, word_index + 1):
					return True
					
				self.visited[row][colm] = False
		return False
		
	# check boudry limits
	def in_board(self, row, colm):
		if row < 0 or row >= len(self.board):
			return False
		if colm < 0 or colm >= len(self.board[0]):
			return False
		return True
	
		
s = Solution()
print s.exist(["ab"], "ba")