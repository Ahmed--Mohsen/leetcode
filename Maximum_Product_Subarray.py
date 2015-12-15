"""

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

"""

class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxProduct(self, A):
		if len(A) == 0:
			return 0
			
		result = A[0]
		
		# stores max product that end at i
		i_max = A[0] 
		
		# stores min product that end at i
		i_min = A[0] 
		
		i = 1
		while i < len(A):
			
			# multiplied by a negative makes big number smaller, small number bigger
			if A[i] < 0:
				i_max, i_min = i_min, i_max
			
			i_max = max(A[i], A[i] * i_max)
			i_min = min(A[i], A[i] * i_min)
			
			result = max(result, i_max)
			i += 1
			
		return result