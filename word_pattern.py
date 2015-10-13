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