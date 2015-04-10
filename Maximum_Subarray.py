class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxSubArray(self, A):
		if len(A) <= 1:
			return A[0]
		max_sum = A[0]
		current_sum = 0
		for a in A:
			current_sum += a
			max_sum = max(max_sum, current_sum)
			current_sum = max(current_sum, 0) #reset if sum if below zero
		return max_sum