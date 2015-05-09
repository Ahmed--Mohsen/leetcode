class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		reverse = 0
		for i in range(32):
			reverse =  (reverse << 1) | ((n >> i) & 1)
		return reverse


s = Solution()
print s.reverseBits(43261596)