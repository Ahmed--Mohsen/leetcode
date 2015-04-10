class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def isValidSudoku(self, board):
		board_size = 9
		rows = [[False]*board_size for count in range(board_size)]
		colms = [[False]*board_size for count in range(board_size)]
		blks = [[False]*board_size for count in range(board_size)]
		
		for i in range(board_size):
			for j in range(board_size):
				if board[i][j] == '.':
					continue
				current = ord(board[i][j]) - ord('1') 
				if rows[i][current] == True or colms[j][current] == True or blks[(i/3)*3+(j/3)][current] == True:
					return False
				rows[i][current] = colms[j][current] = blks[(i/3)*3+(j/3)][current] = True
		return True
					
	def show_sudoku(self, board, rows, colms, blks):
		print "-" * 100
		
		s = " "
		print range(1,10)
		for i in range(9):
			for j in range(9):
				s += "+  " if rows[i][j] else "-  "
			s += "\n "
		print s
		
		print "-" * 100
		
		s = " "
		print range(9)
		for i in range(9):
			for j in range(9):
				s += "+  " if colms[i][j] else "-  "
			s += "\n "
		print s
		
		s = " "
		print range(9)
		for i in range(9):
			for j in range(9):
				s += "+  " if blks[i][j] else "-  "
			s += "\n "
		print s
		
s = Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])