"""

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""

class Solution:
	
	# @return a list of integers
	def generateMatrix(self, n):
		# base case
		if n == 0: return []
			
		matrix = [[0] * n for i in range(n)]
		row_start = 0; row_end = n - 1
		col_start = 0; col_end = n - 1
		num = 1
		
		while row_start <= row_end and col_start <= col_end:
			# move right
			for j in range(col_start, col_end+1):
				matrix[row_start][j] = num
				num += 1
			row_start += 1
		
			# move down
			for i in range(row_start, row_end+1):
				matrix[i][col_end] = num
				num += 1
			col_end -= 1
		
			# move left
			if row_start <= row_end:
				for j in range(col_end, col_start-1, -1):
					matrix[row_end][j] = num
					num += 1
			row_end -= 1
			
			# move up
			if col_start <= col_end:
				for i in range(row_end, row_start-1, -1):
					matrix[i][col_start] = num
					num += 1
			col_start += 1
		
		return matrix
	
	

s = Solution()
print s.generateMatrix(3)