class Solution:
	# @return a list of lists of string
	def totalNQueens(self, n):
		self.columns = [0]*n #row to column mapping for queens positions
		self.result = 0
		self.totalNQueensHelper(0, n)
		return self.result
	
	
	def totalNQueensHelper(self, row, n):
		if row >= n: #all queens placed success
			self.result += 1
			return
		
		#check all columns to add the current queen at row
		for colm in range(n):
			if self.is_safe(row, colm): 
				#add queen
				self.columns[row] = colm
				
				#recurse to next row
				self.totalNQueensHelper(row+1, n)
				
				#backtrack
				self.columns[row] = 0
		
		#no solution found 
		return
			
	def is_safe(self, row, colm):
		for r in range(row):
			c = self.columns[r]
			
			#check same column
			if c == colm:
				return False
			
			#check same diagonal
			if abs(row - r) == abs(colm - c):
				return False
		
		return True

s = Solution()
print s.totalNQueens(4)