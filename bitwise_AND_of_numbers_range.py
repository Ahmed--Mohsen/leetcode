"""

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

"""

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