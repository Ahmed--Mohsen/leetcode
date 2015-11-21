"""

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

"""

class Solution:
	
	# @param {string} s
	# @param {string} t
	# @return {boolean}
	def isIsomorphic(self, s, t):
		# base case
		if len(s) != len(t):
			return False
		
		mapping = {} # from s to t
		reverse_mapping = {} # from t to s
		
		# iterate while checking counters
		for i in range(len(s)):
			if not self.map_char(s[i], t[i], mapping):
				return False
			
			if not self.map_char(t[i], s[i], reverse_mapping):
				return False
			
		return True
		
	def map_char(self, a, b, mapping):
		if not a in mapping:
			mapping[a] = b
		return mapping[a] == b
	

s = Solution()
print s.isIsomorphic("aba", "baa")