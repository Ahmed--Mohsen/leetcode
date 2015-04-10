class Solution:
	# @param s, a string
	# @return an integer
	def lengthOfLastWord(self, s):
		tokens = s.split()
		return len(tokens[-1]) if len(tokens) > 0 else 0
		