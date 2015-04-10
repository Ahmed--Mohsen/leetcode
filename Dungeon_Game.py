class Solution:
	# @param dungeon, a list of lists of integers
	# @return a integer
	def calculateMinimumHP(self, dungeon):
		m = len(dungeon)
		n = len(dungeon[0])
		
		#store the cost to go from cell (i,j) to cell (m-1, i-1)
		dp = [ [0] * n for i in range(m) ]
		
		#to reach end he must at least have a health of 1
		dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
		
		#fill right side
		for i in range(m-2, -1, -1):
			dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
		
		#fill bottom side
		for j in range(n-2, -1, -1):
			dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
		
		#fill the rest of the array
		for i in range(m-2, -1, -1):
			for j in range(n-2, -1, -1):
					dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
					
		return dp[0][0]


s = Solution()
print s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])