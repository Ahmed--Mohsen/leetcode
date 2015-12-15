"""

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]


"""

class Solution:
	
	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):
		# base case
		if len(s) <= 1: return [[s]]
		
		self.is_plandirom_dp = self.build_palindrome_dp(s)
		self.result = []
		self.partition_helper(s, 0, [])
		return self.result
	
	
	def build_palindrome_dp(self, s):
		n = len(s)
		
		# add extra column to handle all indexes inclusive
		memory = [[False] * n for i in range(n, 0, -1)]

		for i in range(n-1, -1, -1):
			for j in range(i, n):
				if s[i] == s[j] and (j - i < 2 or memory[i+1][j-1] == True):
					memory[i][j] = True
		return memory
		
	
	def partition_helper(self, s, start, partitions):
		# all string have been partioned into planidrom substring
		if start >= len(s):
			self.result.append(list(partitions))
			return
		
		for i in range(start, len(s)):
			
			# substring from start to i makes a plandirom
			if self.is_plandirom_dp[start][i] == True:
				
				# add it to current result, substring start:i inclusive
				partitions.append(s[start : i+1])
				
				# recurse to next substring
				self.partition_helper(s, i+1, partitions)
				
				# backtrack
				partitions.pop()
	
		
s = Solution()
x = "bb"
print s.partition(x)
#print s.is_palindrome(x, 1, len(x)-2 )