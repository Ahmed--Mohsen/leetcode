class Solution:
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def rangeBitwiseAnd(self, m, n):
		# x tells which first k-bit m and n start to differ
		x = m ^ n
		
		# set all bits [k, 0] to 1
		mask = 0
		while x:
			mask = (mask << 1) | 1
			x >>= 1
		
		# reverse all bits [k, 0] to 0
		mask = ~mask
		
		return m & n & mask


s = Solution()
print s.rangeBitwiseAnd(5, 7)