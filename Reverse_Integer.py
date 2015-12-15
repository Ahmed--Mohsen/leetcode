"""

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
	
	# @return an integer
	def reverse(self, x):
		# according to the problem int size will be 32 bit
		# using 2's complement => max = 2^31 -1
		MAX_INT = 2**31 - 1
		
		# fetch x's sign
		sign = -1 if x < 0 else 1
		
		# remove x's sign
		x = sign * x
		
		# do the reversal
		ans = 0
		while x > 0:
			ans = (ans * 10) + (x % 10)
			
			# check overflow
			if ans > MAX_INT:
				return 0
			x = x  / 10
		
		# add the sign back
		return sign * ans

s = Solution()
print s.reverse(-123456789)