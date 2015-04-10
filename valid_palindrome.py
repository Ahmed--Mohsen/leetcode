# -*- coding: utf-8 -*-

class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		if len(s) < 2:
			return True
		start = 0 
		end = len(s) - 1
		while start < end:
			while(start < len(s) and not(self.isLetter(s[start])) and not(self.isNumber(s[start]))):
				start = start + 1
			while(end >= 0 and not(self.isLetter(s[end])) and not(self.isNumber(s[end]))):
				end = end - 1
			if start > end: #empty string or with all punc
				return True
			if s[start].lower() != s[end].lower():
				return False
			start = start + 1
			end = end - 1		
		return True	
		#return self.validate(s,0 , len(s) - 1)
	
	def isLetter(self, c):
		return ((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'))
	
	def isNumber(self, c):
		return (c >= '0' and c <= '9')
		
	def validate(self, s, start, end):
		if start > end or start == end:
			return True
		if s[start] != s[end]:
			return False
		return self.validate(s, start + 1, end - 1)
		

s = Solution()
print s.isPalindrome("a.")