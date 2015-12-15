"""

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

"""

class Solution:
	
	# @param    A       a list of integers
	# @param    elem    an integer, value need to be removed
	# @return an integer
	def removeElement(self, A, elem):
		n = len(A)
		
		# base case
		if n == 0: return 0
			
		index = 0
		for i in range(n):
			if A[i] != elem:
				A[index] = A[i]
				index += 1
		
		return index
		
		
s = Solution()
print s.removeElement([2], 6)