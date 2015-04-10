class Solution:
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		rows = len(grid)
		colms = len(grid[0])
		
		#fill bottom row  
		for j in range(colms - 2, -1, -1):
			grid[rows - 1][j] += grid[rows - 1][j+1]
		
		#fil right colmn
		for i in range(rows - 2, -1, -1):
			grid[i][colms - 1] += grid[i+1][colms - 1]
		
		#get optimal path
		for i in range(rows - 2, -1, -1):
			for j in range(colms - 2, -1, -1):
				grid[i][j] += min(grid[i+1][j], grid[i][j+1])
		
		return grid[0][0]


s = Solution()
print s.minPathSum([[1,2],[5,6],[1,1]])