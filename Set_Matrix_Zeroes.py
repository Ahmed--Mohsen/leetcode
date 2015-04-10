class Solution:
	# @param matrix, a list of lists of integers
	# RETURN NOTHING, MODIFY matrix IN PLACE.
	def setZeroes(self, matrix):
		height = len(matrix)
		width = len(matrix[0])
		if height == 0 or width == 0:
			return
		
		#check if first row or colmn will be set to zeros
		has_zero_first_row = False
		has_zero_first_colm = False
		
		#Does first row have zero?
		for j in range(width):
			if matrix[0][j] == 0:
				has_zero_first_row = True
				break
		
		#Does first colm have zero?
		for i in range(height):
			if matrix[i][0] == 0:
				has_zero_first_colm = True
				break
		
		#save zero positions in first row and colm
		for i in range(height):
			for j in range(width):
				if matrix[i][j] == 0:
					matrix[i][0] = 0
					matrix[0][j] = 0
		
		#set other elemets to zero rather than the first row and colm
		for i in range(1, height):
			for j in range(1, width):
				if matrix[i][0] == 0 or matrix[0][j] == 0:
					matrix[i][j] = 0
					
		#check first and last row
		if has_zero_first_row:
			for j in range(width):
				matrix[0][j] = 0
		if has_zero_first_colm:
			for i in range(height):
				matrix[i][0] = 0