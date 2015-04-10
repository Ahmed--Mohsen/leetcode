class Solution:
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		dp = [0]*(n+3) # the extra 2 for the base cases
		dp[0] = 0
		dp[1] = 1
		dp[2] = 2
		
		for i in range(3,n+1):
			dp[i] = dp[i-1] + dp[i-2]
		
		return dp[n]
	
s = Solution()
print s.climbStairs(3)