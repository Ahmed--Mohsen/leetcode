class Solution:
	# @return a list of lists of string
	def solveNQueens(self, n):
		self.board = [['.']*n for i in range(n)]
		self.columns = [0]*n #row to column mapping for queens positions
		self.result = []
		self.solveNQueensHelper(0, n)
		return self.result
	
	
	def solveNQueensHelper(self, row, n):
		if row >= n: #all queens placed success
			self.add_result()
			return
		
		#check all columns to add the current queen at row
		for colm in range(n):
			if self.is_safe(row, colm): #add queen
				self.columns[row] = colm
				self.board[row][colm] = 'Q'
				#self.print_board()
				
				#recurse to next row
				self.solveNQueensHelper(row+1, n)
				
				#failure backtrack
				self.columns[row] = 0
				self.board[row][colm] = '.'
		
		#no solution found 
		return False			
			
	def is_safe(self, row, colm):
		# check prev rows
		for r in range(row):
			c = self.columns[r]
			
			#check same column
			if c == colm:
				return False
			
			#check same diagonal
			if abs(row - r) == abs(colm - c):
				return False
		
		return True	
		
	def add_result(self):
		sub_result = []
		for row in self.board:
			sub_result.append("".join(row))
		self.result.append(sub_result)
		

	def print_board(self):
		print "\n"
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				print self.board[i][j], " ",
			print "\n"

s = Solution()
print s.solveNQueens(10)