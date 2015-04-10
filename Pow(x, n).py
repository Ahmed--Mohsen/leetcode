class Solution:
	# @param x, a float
	# @param n, a integer
	# @return a float
	def pow(self, x, n):
		if n < 0:
			n = -1 * n
			x = 1 / x
		
		return self.pow_helper(x,n)
	
	def pow_helper(self, x, n):
		if n == 0:
			return 1
		
		half_pow = self.pow_helper(x, n/2)
		if n % 2 == 0:
			return half_pow * half_pow
		else:
			return x * half_pow * half_pow


s = Solution()
print s.pow(3,7)