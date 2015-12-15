"""

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

"""

class Solution:
	
	# @param A, a list of integers
	# @return an integer
	def maxSubArray(self, A):
		
		# base case
		if len(A) <= 1: return A[0]
		
		# apply kaden algorithm
		max_sum = A[0] # actual maximum
		current_sum = 0 # max so far
		
		for a in A:
			current_sum += a
			
			# update the max sum as long as current_sum is bigger
			max_sum = max(max_sum, current_sum)
			
			# reset if sum is below zero
			current_sum = max(current_sum, 0) 
		return max_sum