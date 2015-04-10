class Solution:
	# @param board, a 9x9 2D array
  # Solve the Sudoku by modifying the input board in-place.
  # Do not return any value.
	def solveSudoku(self, board):
		self.board_size = 9
		self.board = board
		self.rows = [[False]*self.board_size for count in range(self.board_size)]
		self.colms = [[False]*self.board_size for count in range(self.board_size)]
		self.blks = [[False]*self.board_size for count in range(self.board_size)]
		self.set_boundries()
		self.solve_helper(0, 0)
		
		
	def solve_helper(self, row, colm):
		if row >= self.board_size: #end reached successufully
			return True
		
		#prepare next indexes to be visited
		next_row = row if colm < self.board_size - 1 else row + 1
		next_colm = colm + 1 if colm < self.board_size - 1 else 0
		
		if self.board[row][colm] == '.': #try to place a valid number here
			for i in range(9): # try from 0 => 8 (1 => 9)
				if self.rows[row][i] == True or self.colms[colm][i] == True or self.blks[(row/3)*3+(colm/3)][i] == True:
					continue
				#found a match
				board_row = list(self.board[row])
				board_row[colm] = str(i+1)
				self.board[row] = board_row
				self.rows[row][i] = self.colms[colm][i] = self.blks[(row/3)*3+(colm/3)][i] = True
				
				#try next cell after adding i
				result = self.solve_helper(next_row, next_colm)
				if result == True:
					return True
					
				#backtrack
				self.rows[row][i] = self.colms[colm][i] = self.blks[(row/3)*3+(colm/3)][i] = False
				self.board[row][colm] = '.'
		else:
			return self.solve_helper(next_row, next_colm)
		return False #no solution found
		
	def set_boundries(self):
		for i in range(self.board_size):
			for j in range(self.board_size):
				if self.board[i][j] == '.':
					continue
				current = ord(self.board[i][j]) - ord('1') 
				self.rows[i][current] = self.colms[j][current] = self.blks[(i/3)*3+(j/3)][current] = True
					
	def show_sudoku(self):
		print "-" * 100
		
		s = " "
		for i in range(self.board_size):
			for j in range(self.board_size):
				s += self.board[i][j]+" "
			s += "\n "
		print s
		"""
		s = " "
		print range(1,10)
		for i in range(9):
			for j in range(9):
				s += "+  " if self.rows[i][j] else "-  "
			s += "\n "
		print s
		
		print "-" * 100
		
		s = " "
		print range(9)
		for i in range(9):
			for j in range(9):
				s += "+  " if self.colms[i][j] else "-  "
			s += "\n "
		print s
		
		s = " "
		print range(9)
		for i in range(9):
			for j in range(9):
				s += "+  " if self.blks[i][j] else "-  "
			s += "\n "
		print s
		"""

s = Solution()
print s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])