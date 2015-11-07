"""

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

class Solution:
	
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		
		# dp[i] = number of ways to climb i stairs
		# the extra 3 for the base cases
		dp = [0]*(n+3) 
		dp[0] = 0
		dp[1] = 1
		dp[2] = 2
		
		for i in range(3,n+1):
			dp[i] = dp[i-1] + dp[i-2]
		
		return dp[n]
	
s = Solution()
print s.climbStairs(3)