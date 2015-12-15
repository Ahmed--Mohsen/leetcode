"""

Given an integer, write a function to determine if it is a power of two.

"""

class Solution(object):
	
	"""
	:type n: int
	:rtype: bool
	"""
	def isPowerOfTwo(self, n):
		# only positive numbers are allowed
		if n <= 0:
			return False
		
		# only power of two differ in all ones with
		# its prev number i.e. 1000 , 0111
		return n & (n - 1) == 0