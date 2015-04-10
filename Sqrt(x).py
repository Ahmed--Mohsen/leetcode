class Solution:
	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
		if x == 0:
			return 0
		return self.sqrt_helper(x, 1, x)
	
	def sqrt_helper(self, x, start, end):
		if start > end:
			return -1
		middle = (start+end)/2
		square = middle * middle
		next_square = (middle + 1) * (middle + 1)
		if square == x or (square < x and x < next_square):
			return middle
		if square > x:
			return self.sqrt_helper(x, start, middle - 1)
		else:
			return self.sqrt_helper(x, middle + 1, end)

s = Solution()
print s.sqrt(2147395599)