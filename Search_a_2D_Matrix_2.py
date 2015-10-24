class Solution:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		if len(matrix) == 0:
			return False
		
		rows = len(matrix)
		colms = len(matrix[0])
		
		# out of range case
		if matrix[0][0] > target or target > matrix[rows-1][colms-1]:
			return False
		
		row = 0
		colm = colms - 1
		
		# step-wise linear search
		while row < rows and colm >= 0:
			# target found
			if target == matrix[row][colm]:
				return True
			
			# search for next move
			if target > matrix[row][colm]:
				row += 1
			else: #target < matrix[row][colm]
				colm -= 1
		
		return False
