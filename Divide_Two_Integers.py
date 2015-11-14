"""

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

"""

class Solution:
	
	# @return an integer
	def divide(self, dividend, divisor):
		p = abs(dividend)
		q = abs(divisor)
		ans = 0
		
		while p >= q:
			counter = 0
			while p >= (q << counter): # detect 2^n that p is divisible by
				counter += 1
			ans += 1 << (counter - 1)
			p -= q << (counter - 1)
			
		if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
			ans = -ans
		
		return ans