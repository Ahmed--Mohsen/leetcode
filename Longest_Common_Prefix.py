class Solution:
	# @return a string
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ""
		
		index = -1
		done = False
		while not(done):
			index += 1
			if index > len(strs[0]) - 1:
				break
			current_char = strs[0][index]
			for i in range(1, len(strs)):
				str = strs[i]
				if len(str) <= index or str[index] != current_char:
					done = True
					break
		return strs[0][0:index]


s = Solution()
print s.longestCommonPrefix(["abc", "abvdf", "abre"])
		