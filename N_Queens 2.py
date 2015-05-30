class Solution:
	# @return a list of lists of string
	def totalNQueens(self, n):
		# row to column mapping for queens positions
		self.columns = [0] * n 
		
		return self.totalNQueensHelper(0, n)
	
	def totalNQueensHelper(self, row, n):
		# all queens placed success
		if row >= n: 
			return 1
		
		# check all columns to add the current queen at row
		solutions = 0
		for colm in range(n):
			if self.is_safe(row, colm): 
				# add queen
				self.columns[row] = colm
				
				# recurse to next row
				solutions += self.totalNQueensHelper(row + 1, n)
				
				# backtrack
				self.columns[row] = 0
		
		# return all solutions found for current row
		return solutions
			
	def is_safe(self, row, colm):
		# look back at already added quens
		for r in range(row):
			c = self.columns[r]
			
			# check same column
			if c == colm:
				return False
			
			# check same diagonal
			if abs(row - r) == abs(colm - c):
				return False
		
		return True

s = Solution()
print s.totalNQueens(4)