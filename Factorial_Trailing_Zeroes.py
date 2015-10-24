class Solution:
	# @return an integer
	def trailingZeroes(self, n):
		zeros = 0 # zeros = n/5 + n/25 + n/125 + ...
		
		# zeros can be made by multipying 10 (2*5)
		# number of 2's (even numbers) will always 
		# be larger than 5
		while n/5:
			zeros += n/5
			n /= 5
		return zeros
		

s = Solution()
print s.trailingZeroes(25)