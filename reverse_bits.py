"""

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

"""

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