"""

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

"""

class Solution:
	# @return a list of lists of string
	def totalNQueens(self, n):
		# flag if a certain column is empty
		self.columns = [True] * n
		
		# flag if a 45 diagonal is empty (row+colm)
		self.diagonal_45 = [True] * (2 * n - 1)
		
		# flag if a 135 diagonal is empty (row-colm)
		# normalize to zero => (n-1 + row-colm)
		self.diagonal_135 = [True] * (2 * n - 1)
		
		return self.totalNQueensHelper(0, n)
	
	def totalNQueensHelper(self, row, n):
		# all queens placed success
		if row == n: 
			return 1
		
		# check all columns to add the current queen at row
		solutions = 0
		for colm in range(n):
			if self.is_safe(row, colm): 
				
				# add queen
				self.columns[colm] = self.diagonal_45[row + colm] = self.diagonal_135[n - 1 + row - colm ] = False
				
				# recurse to next row
				solutions += self.totalNQueensHelper(row + 1, n)
				
				# backtrack
				self.columns[colm] = self.diagonal_45[row + colm] = self.diagonal_135[n - 1 + row - colm ] = True
		
		# return all solutions found for current row
		return solutions
			
	def is_safe(self, row, colm):
		n = len(self.columns)
		
		# check same column and diagonals
		return self.columns[colm] and self.diagonal_45[row + colm] and self.diagonal_135[n - 1 + row - colm ]
		

s = Solution()
print s.totalNQueens(4)