class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of integers
	def spiralOrder(self, matrix):
		if len(matrix) == 0:
			return []
			

		result = []
		row_start = 0; row_end = len(matrix) - 1
		col_start = 0; col_end = len(matrix[0]) - 1
		
		while row_start <= row_end and col_start <= col_end:
			#move right
			for j in range(col_start, col_end+1):
				result.append(matrix[row_start][j])
			row_start += 1
		
			#move down
			for i in range(row_start, row_end+1):
				result.append(matrix[i][col_end])
			col_end -= 1
		
			#move left
			if row_start <= row_end:
				for j in range(col_end, col_start-1, -1):
					result.append(matrix[row_end][j])
			row_end -= 1
			
			#move up
			if col_start <= col_end:
				for i in range(row_end, row_start-1, -1):
					result.append(matrix[i][col_start])
			col_start += 1
		
		
		return result
	
	

s = Solution()
print s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])