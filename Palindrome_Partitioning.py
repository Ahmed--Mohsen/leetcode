class Solution:
	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):
		if len(s) <= 1:
			return [[s]]
		
		self.is_plandirom_dp = self.build_palindrome_dp(s)
		self.result = []
		self.partition_helper(s, 0, [])
		return self.result
	
	
	def build_palindrome_dp(self, s):
		n = len(s)
		memory = [[False]*n for i in range(n, 0, -1)]

		for i in range(n-1, -1, -1):
			for j in range(i, n):
				if s[i] == s[j] and (j - i < 2 or memory[i+1][j-1] == True):
					memory[i][j] = True
		return memory
		
	
	def partition_helper(self, s, start, partitions):
		if start >= len(s):
			self.result.append(list(partitions))
			return
		
		for i in range(start, len(s)):
			#if self.is_palindrome(s, start, i):
			if self.is_plandirom_dp[start][i] == True:
				partitions.append(s[start:i+1])
				self.partition_helper(s, i+1, partitions)
				partitions.pop()
	
	def is_palindrome(self, s, start, end):
		while start < end:
			if s[start] != s[end]:
				return False
			start += 1
			end -= 1
		return True
		
s = Solution()
x = "bb"
print s.partition(x)
#print s.is_palindrome(x, 1, len(x)-2 )