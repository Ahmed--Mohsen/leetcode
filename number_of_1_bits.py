class Solution:
	# @param n, an integer
	# @return an integer
	def hammingWeight(self, n):
		count = 0
		
		while n:
			# n & 1 would return 1 only if least bit is one
			count += n & 1
			
			# left shift n by one
			n >>= 1
		
		return count
		

s = Solution()
print s.hammingWeight(11)