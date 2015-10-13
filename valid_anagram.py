class Solution(object):
	
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	def isAnagram(self, s, t):
		# base case ... different strings
		if len(s) != len(t):
			return False
		
		# assuming all chars are lower chars
		chars = [0] * 26
		
		# fill the char bucket
		for i in range(len(s)):
			chars[ord(s[i]) - ord('a')] += 1
		
		# remove from respective char bucket
		for i in range(len(t)):
			chars[ord(t[i]) - ord('a')] -= 1
		
		# for s and t to be angrams buckets needs to be empty
		for bucket in chars:
			if bucket != 0: return False
		
		# all is well
		return True