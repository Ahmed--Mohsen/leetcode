"""

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.

"""

class Solution:
	# @param {character[][]} matrix
	# @return {integer}
	def maximalSquare(self, matrix):
		rows = len(matrix)
		colms = len(matrix[0]) if rows else 0
		max_size = 0
		
		# base case (empty matrix)
		if rows == 0 or colms == 0:
			return 0
		
		# size[i][j] stores the max square size that can be made at (i,j)
		size = [[ord(char)-ord('0') for char in array] for array in matrix]
		
		# max size for most right colm
		max_size = max( size[i][colms-1] for i in range(rows) )
		
		# max size for lower row
		max_size = max(max_size, max( size[rows-1][j] for j in range(colms) ) )
		
		# size for the rest of the matrix
		for i in range(rows-2, -1, -1):
			for j in range(colms-2, -1, -1):
				if size[i][j] == 1:
					size[i][j] = min(size[i+1][j], size[i][j+1], size[i+1][j+1]) + 1
					max_size = max(max_size, size[i][j])

		return max_size * max_size

		
		
def print_list(matrix):
	for array in matrix:
		print array
			
s = Solution()
x = [
			['1', '0', '1', '0', '0'],
			['1', '0', '1', '1', '1'],
			['1', '1', '1', '1', '1'],
			['1', '0', '0', '1', '0']
		]
print s.maximalSquare(x)
		
		