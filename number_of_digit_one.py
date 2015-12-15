"""

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.

"""
class Solution(object):
	
	"""
	:type n: int
	:rtype: int
	"""
	def countDigitOne(self, n):
		
		# base cases
		if n <= 0: return 0

		if n < 10: return 1
		
		# get the max power base of 10 that is less than n
		base = 1
		
		# the left side of n after splitting
		r = n
		
		while r >= 10:
			base *= 10
			r /= 10
		
		# the right side of n after splitting
		m = n % base
		
		# calculate one strikes like (1000, 1999)
		# 1000 => 1999 = 1000 1s + ones(999)
		# 1000 => 1800 = (1800 - 1000 + 1) 1s + ones(800)
		full_cycle = (n - base + 1) if (r == 1) else base

		# recurse for the r part and m part
		return self.countDigitOne(base - 1) * r + full_cycle + self.countDigitOne(m)
		

s = Solution()
print s.countDigitOne(321)