class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return a list of length 2, [index1, index2]
	def searchRange(self, A, target):
		n = len(A)
		result = [-1, -1]
		if n == 0:
			return result
		
		left = self.first_occurance(A, target)
		if left < n and A[left] == target: #element is present
			right = self.first_occurance(A, target + 1)
			return [left, right - 1]
		else: #no occurance occured
			return [-1 , -1]
			
	
	#return the index of the first element to be equal to target
	def first_occurance(self, A, target):
		start = 0
		end = len(A) - 1
		while start <= end:
			mid = ( start + end ) / 2
			if A[mid] < target:
				start = mid + 1
			else:
				end = mid - 1
		return start
		

s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 8)