"""

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

"""

class Solution:
	
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		l1 = len(s1); l2 = len(s2); l3 = len(s3)
		
		if l1+l2 != l3:
			return False
		
		# dp[i][j] ==> s1[0:i-1] and s2[0:j-1] interleave at s3[0:i+j-1]
		dp = [[False]*(l2+1) for i in range(l1+1)]
		
		# s1 and s2 are empty
		dp[0][0] = True 
		
		# when s1 is empty ... i = 0
		for j in range(1, l2+1):
			dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
			
		# when s2 is empty ... j = 0
		for i in range(1, l1+1):
			dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
		
		# the general case s1 and s2 are full	
		for i in range(1, l1+1):
			for j in range(1, l2+1):
					dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
	
		return dp[l1][l2]



s = Solution()
print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
		
		