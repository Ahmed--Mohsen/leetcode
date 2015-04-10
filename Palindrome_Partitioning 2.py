class Solution:
	# @param s, a string
	# @return an integer
	def minCut(self, s):
		if len(s) == 0:
			return 0
		return self.build_palindrome_dp(s)[0]
	
	def build_palindrome_dp(self, s):
		n = len(s)
		memory = [[False]*n for i in range(n, 0, -1)]
		min_cut = [0] * n
		
		for i in range(n-1, -1, -1):
			min_cut[i] = n - i - 1 #worest case for searching at pos i
			for j in range(i, n):
				if s[i] == s[j] and (j - i < 2 or memory[i+1][j-1] == True):
					memory[i][j] = True
					if j == n - 1: #substring from i to j is palindrome
						min_cut[i] = 0
					else: #try cutting at pos j and see if its better
						min_cut[i] = min(min_cut[i], min_cut[j+1] + 1)
						
		return min_cut
		
	
		
s = Solution()
x = "bb"
print s.minCut(x)
#print s.is_palindrome(x, 1, len(x)-2 )