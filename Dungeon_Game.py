"""

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

"""

class Solution:
	# @param dungeon, a list of lists of integers
	# @return a integer
	def calculateMinimumHP(self, dungeon):
		m = len(dungeon)
		n = len(dungeon[0])
		
		#store the cost to go from cell (i,j) to cell (m-1, n-1)
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