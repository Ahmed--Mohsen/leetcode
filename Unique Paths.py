class Solution:
	# @return an integer
	def uniquePaths(self, m, n):
		grid = [[1]*n for i in range(m)]
		
		for i in range(1,m):
			for j in range(1,n):
				grid[i][j] = grid[i-1][j] + grid[i][j-1]
		
		return grid[m-1][n-1]


s = Solution()
print s.uniquePaths(3,3)