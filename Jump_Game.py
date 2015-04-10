class Solution:
	# @param A, a list of integers
	# @return a boolean
	def canJump(self, A):
		n = len(A)
		jumps = 0
		i = 0
		
		while i < n and i <= jumps:
			jumps = max(jumps, A[i] + i)
			i += 1
		
		return jumps >= n - 1
				