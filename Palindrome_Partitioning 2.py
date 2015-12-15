"""

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""

class Solution:
	
	# @param s, a string
	# @return an integer
	def minCut(self, s):
		# base case
		if len(s) == 0: return 0
		
		return self.build_palindrome_dp(s)[0]
	
	def build_palindrome_dp(self, s):
		n = len(s)
		
		# memory[i][j] = true means s[i:j+1] is a plaindrom
		memory = [ [False] * n for i in range(n, 0, -1) ]
		
		# min cut for s[i..n-1]
		min_cut = [0] * n
		
		for i in range(n-1, -1, -1):
			
			# worst case the substring[i:n-1] needs to be cut to substring of 
			# each of length 1 ... i => n - 1 : n - i - 1 
			min_cut[i] = n - i - 1 
			for j in range(i, n):
				
				# check if s[i:j] is plindrome
				if s[i] == s[j] and (j - i < 2 or memory[i+1][j-1] == True):
					memory[i][j] = True
					
					# substring from i to n-1 is palindrome
					if j == n - 1: 
						min_cut[i] = 0
						
					# try cutting at pos j and see if its better s[i:j] is palindrom
					# so min cut will be min_cut[i] = 0 (cause already plaindrome) + min_cut(j+1) + 1
					else: 
						min_cut[i] = min(min_cut[i], min_cut[j+1] + 1)
						
		return min_cut
		
	
		
s = Solution()
x = "bba"
print s.minCut(x)