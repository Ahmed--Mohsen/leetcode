class Solution:
	# @param A, a list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		n = len(A)
		if n == 0:
			return 1
		
		#k is the len of the positive subarray of A
		k = self.partition(A)
		
		#the first posistive number must be between [1, k]
		#A[i] = -A[i] means i+1 exist in A
		for i in range(k):
			temp = abs(A[i])
			if temp <= k and A[temp - 1] > 0: 
				A[temp - 1] = -1 * A[temp - 1] #mark visited
		
		#search for A[i] which is not visited yet
		for i in range(k):
			if A[i] > 0: 
				return i + 1
		
		#all numbers exist from [1, k] ... so missing is k+1
		return k + 1


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
	
	def swap(self, array, i, j):
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
		

s = Solution()
print s.firstMissingPositive([3,4,-1,1])