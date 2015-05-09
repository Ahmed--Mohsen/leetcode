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