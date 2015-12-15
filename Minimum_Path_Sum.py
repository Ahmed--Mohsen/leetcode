"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""

############################ O(n) Space Solution ############################
class Solution:
	
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		rows = len(grid)
		colms = len(grid[0])
		
		# looking at the O(n^2) solution each state depends on
		# current column j and right column j+1 
		dp = [0] * rows
		
		# fill most right column state
		dp[rows-1] =  grid[rows-1][colms-1]
		for i in range(rows - 2, -1, -1):
			dp[i] = grid[i][colms-1] + dp[i+1]
		
		# for each column with right column state as dp
		for j in range(colms - 2, -1, -1):
			
			# same as filling the bottom row in the O(n^2) solution
			dp[rows-1] += grid[rows-1][j]
			
			for i in range(rows - 2, -1, -1):
			
				# dp[i]: represents state in the right column, 
				# dp[i+1]: represents state in the below row
				dp[i] = min(dp[i], dp[i+1]) + grid[i][j]
		
		return dp[0]
		

############################ O(n^2) Space Solution ############################
class Solution2:
	
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		rows = len(grid)
		colms = len(grid[0])
		
		# fill bottom row  
		for j in range(colms - 2, -1, -1):
			grid[rows - 1][j] += grid[rows - 1][j+1]
		
		# fill right colmn
		for i in range(rows - 2, -1, -1):
			grid[i][colms - 1] += grid[i+1][colms - 1]
		
		# get optimal path
		for i in range(rows - 2, -1, -1):
			for j in range(colms - 2, -1, -1):
				grid[i][j] += min(grid[i+1][j], grid[i][j+1])
		
		return grid[0][0]


s = Solution()
print s.minPathSum([[1,2],[5,6],[1,1]])