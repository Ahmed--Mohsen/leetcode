class Solution:
	# @return an integer
	def reverse(self, x):
		sign = -1 if x < 0 else 1
		x = sign * x		
		ans = 0
		while x > 0:
			ans = (ans * 10) + (x % 10)
			x = x  / 10
		return sign * ans

s = Solution()
print s.reverse(-123456789)