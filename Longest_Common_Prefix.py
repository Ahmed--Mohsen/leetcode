"""

Write a function to find the longest common prefix string amongst an array of strings.

"""

class Solution:
	
	# @return a string
	def longestCommonPrefix(self, strs):
		# base case
		if len(strs) == 0: return ""
		
		# the result would be either the first string or part of it
		prefix = strs[0]
		
		for i in range(len(prefix)):
			c = prefix[i]
			
			# check that c exist in i position for all other strings
			for s in strs:
				if i >= len(s) or s[i] != c:
					return prefix[0:i]
		
		# first string is the actual prefix
		return prefix
		

s = Solution()
print s.longestCommonPrefix(["abc", "abcvdf", "abcre"])
		