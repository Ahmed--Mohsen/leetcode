class Solution:
	# @param haystack, a string
	# @param needle, a string
	# @return a string or None
	def strStr(self, haystack, needle):
		#base cases
		if len(needle) == 0:
			return haystack
		if len(haystack) == 0:
			return None
			
		shifts = self.create_shifts_arr(needle)
		i = 0; j = 0

		while i < len(haystack):
			while j >= 0 and haystack[i] != needle[j]:
				j = shifts[j]
			i += 1; j += 1
			if j >= len(needle):
				return haystack[(i-j):]
		return None
	
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
		

s = Solution()
print s.strStr("mississippi", "issip")