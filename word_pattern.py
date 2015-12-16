"""

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""

class Solution(object):
	
	"""
	:type pattern: str
	:type str: str
	:rtype: bool
	"""
	def wordPattern(self, pattern, str):
		# base case
		if not pattern or len(pattern) == 0:
			return len(str) == 0
		
		memo = {}
		strs = str.split(" ")
		
		# another base case
		if len(strs) != len(pattern):
			return False
		
		for i in range(len(strs)):
			current = strs[i]
			# exist before
			if current in memo:
				if pattern[i] != memo[current]:
					return False
			
			# new sub pattern
			else:
				if pattern[i] in memo.values():
					return False
				memo[current] = pattern[i]
		
		return True