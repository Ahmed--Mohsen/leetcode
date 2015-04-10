class Solution:
	# @return an integer
	def isPalindrome(self, x):
		if x < 0:
			return False
		normal = x
		reverse = 0
		while x > 0:
			reverse = (reverse * 10) + (x % 10)
			x = x  / 10
		return normal == reverse

s = Solution()
print s.isPalindrome(1321)