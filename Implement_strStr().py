"""

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""

################################# KMP Solution #################################
class Solution:
	
	# @param haystack, a string
	# @param needle, a string
	# @return a string or None
	def strStr(self, haystack, needle):
		# base cases
		if len(needle) == 0: return 0
		if len(haystack) == 0: return -1
			
		shifts = self.create_shifts_arr(needle)
		i = 0; j = 0

		while i < len(haystack):
			while j >= 0 and haystack[i] != needle[j]:
				j = shifts[j]
			i += 1; j += 1
			if j >= len(needle):
				return haystack[(i-j):]
		return None
	
	# shifts array: proper prefix in the (sub)pattern that 
	# matches a proper suffix in the same (sub)pattern.
	def create_shifts_arr(self, pattern):
		M = len(pattern)
		shifts = [0] * (M+1)
		shifts[0] = -1
		
		i = 0; j = -1
		while i < M:
			while j >= 0 and pattern[i] != pattern[j]:
				j = shifts[j]
			
			i += 1; j += 1
			shifts[i] = j
		return shifts
		

################################# Brute force Solution #################################
class Solution:
	
	# @param haystack, a string
	# @param needle, a string
	# @return a string or None
	def strStr(self, haystack, needle):
		m = len(haystack)
		n = len(needle)
		
		# base cases
		if n == 0: return 0
		if m == 0: return -1
		
		for i in range(m - n + 1):	
			for j in range(n):
				
				# match failed
				if haystack[i+j] != needle[j]: break
				
				# sucees
				if j == n - 1: return i
				
		# failure
		return -1

s = Solution()
print s.strStr("mississippi", "issip")