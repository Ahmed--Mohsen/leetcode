class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		if len(s) < 2: #base case
			return len(s)
		
		max_len = 1
		appeared = {}
		start = 0
		for i in range(0, len(s)):
			end = -1 if not(s[i] in appeared) else appeared[s[i]]
			appeared[s[i]] = i
			if start <= end:
				start = end + 1
			max_len = max(max_len, i - start + 1)
		return max_len


s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")
		