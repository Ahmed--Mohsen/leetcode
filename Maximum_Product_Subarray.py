class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxProduct(self, A):
		if len(A) == 0:
			return 0
			
		result = A[0]
		i_max = A[0] #stores max product that end at i
		i_min = A[0] #stores min product that end at i
		
		i = 1
		while i < len(A):
			
			#multiplied by a negative makes big number smaller, small number bigger
			if A[i] < 0:
				i_max, i_min = i_min, i_max
			
			i_max = max(A[i], A[i] * i_max)
			i_min = min(A[i], A[i] * i_min)
			
			result = max(result, i_max)
			i += 1
			
		return result