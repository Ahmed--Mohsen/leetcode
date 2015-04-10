class Solution:
	# @param board, a list of lists of 1 length string
	# @param word, a string
	# @return a boolean
	def exist(self, board, word):
		if len(word) == 0 or len(board) == 0:
			return False
		self.board = board
		self.word = word
		self.visited = [[False]*len(board[0]) for i in range(len(board))]

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