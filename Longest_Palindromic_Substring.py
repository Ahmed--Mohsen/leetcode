"""

Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.

"""

      ########################## Iterative solution ##########################
########################## memory = o(1) ... time = O(n^2) ##########################
class Solution:
	
	# @return a string
	def longestPalindrome(self, s):
		if len(s) <= 1: #base case
			return s
		
		#base case
		longest = s[0:1]
		
		for i in range(len(s)):
			# check even plandirom that centered at i, i+1
			even = self.expand(s, i, i+1)
			if len(even) > len(longest):
				longest = even
			
			# check odd plandirom that centered at i
			odd = self.expand(s, i, i)
			if len(odd) > len(longest):
				longest = odd
			
		return longest
		
	def expand(self, s, left, right):
		n = len(s)
		while left >= 0 and right < n and s[left] == s[right]:
			left -= 1
			right +=1
		return s[left+1:right]
		



 ########################## Dynamic programming ... Got TLE ##########################
########################## memory = o(n^2) ... time = O(n^2) ##########################
class Solution:
	# @return a string
	def longestPalindrome(self, s):
		if len(s) <= 1: #base case
			return s
		
		memory = [[False]*len(s) for i in range(len(s), 0, -1)]
		
		#every string of length 1 is plandirom
		for i in range(len(s)):
			memory[i][i] = True
		start = 0
		end = 0

		for step in range(2,len(s)+1):
			for i in range(len(s)-step+1):
				j = i + step - 1
				if s[i] == s[j] and memory[i+1][j-1] == True:
					memory[i][j] = True
					start = i
					end = j
		
		return s[start:end+1]		
		


s = Solution()
print s.longestPalindrome("12321s") 
		