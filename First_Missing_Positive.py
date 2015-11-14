"""

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""

class Solution:
	
	# @param A, a list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		
		# treat a as a map were A[i-1] = i only if 
		# i exist in A
		n = len(A)
		for i in range(n):
			
			# only process A[i] if in range [1,n]
			while A[i] > 0 and A[i] <= n and A[A[i] - 1] != A[i]:
				self.swap(A, i, A[i] - 1)
		
		# check if the missing in range [1,n]
		for i in range(n):
			if A[i] != i + 1:
				return i + 1
			
		# all numbers exist from [1, n] ... so missing is n+1
		return n + 1

	# swap two elements at position i, j
	def swap(self, array, i, j):
		temp = array[i]
		array[i] = array[j]
		array[j] = temp



############################### Another Solution ###############################
class Solution:
	
	# @param A, a list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		n = len(A)
		if n == 0:
			return 1
		
		# k is the len of the positive subarray of A
		k = self.partition(A)
		
		# the first positive number must be between [1, k+1]
		# A[i] = -A[i] means i+1 exist in A
		for i in range(k):
			temp = abs(A[i]) # temp = 1, its position = 0
			if temp <= k and A[temp - 1] > 0: 
				A[temp - 1] = -1 * A[temp - 1] # mark visited

		# search for A[i] which is not visited yet
		for i in range(k):
			if A[i] > 0: 
				return i + 1 # zero based

		# all numbers exist from [1, k] ... so missing is k+1
		return k + 1

	# partition the array and add all positive 
	# number at the beginning and the negatives
	# at the end
	def partition(self, array):
		left = 0
		right = len(array) - 1
		
		while left <= right:
			while left <= right and array[left] > 0:
				left += 1
			while left <= right and array[right] <= 0:
				right -= 1
			if left < right:
				self.swap(array, left, right)
		return left
		
	# swap two elements at position i, j
	def swap(self, array, i, j):
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
		

s = Solution()
print s.firstMissingPositive([2])